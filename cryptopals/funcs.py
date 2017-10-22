import string
import urllib
import random
from Crypto.Cipher import AES
import struct
#1
def hex2b64(s):
    return s.decode('hex').encode('base64')[:-1]

def bytify(st):
    return [ord(i) for i in st.decode('hex')]

def unbytify(st):
    return ''.join([chr(i).encode('hex') for i in st])

#2
#why would my xor only work on hex encoded stuff.. that is so stupid and will lead to lots of useless conversions:D lool let's leave it like this anyway!
def xor(st1,st2):
    st1=bytify(st1)
    
    st2=bytify(st2)
    l=len(st2)
    
    return unbytify([st1[i] ^ st2[i%l] for i in range(len(st1))])

#3
def engfreq(st,notprintablesig=5):
    return 1.0*(len(filter(lambda x: x in string.ascii_letters,st))-notprintablesig*len(filter(lambda x: x not in string.printable,st)))/len(st)#the -5

def solve3(a='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736',freq=5):
    
    opts = []
    for i in range(256):
        opts.append((i,engfreq(xor(a,chr(i).encode('hex')).decode('hex'),freq)))
    best = max(opts, key=lambda x: x[1])
    
    return best,xor(a,chr(best[0]).encode('hex')).decode('hex')

#4
def solve4():
    a = urllib.urlopen('http://cryptopals.com/static/challenge-data/4.txt').read().split('\n')
    opts = []
    for i in a:
        opts.append(solve3(i))
    return max(opts,key=lambda x: x[0][1])

#5
def solve5():
    return xor('''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''.encode('hex'),'ICE'.encode('hex'))

#6
def hammingdst(st1,st2):
    return sum([len(filter(lambda x: x=='1',bin(ord(st1[i])^ord(st2[i])))) for i in range(len(st1))])

def solve6():
    print hammingdst('this is a test','wokka wokka!!!')
    opts=[]
    a = urllib.urlopen('http://cryptopals.com/static/challenge-data/6.txt').read().decode('base64')
    for i in range(2,40):
        opts.append((i,(hammingdst(a[:i],a[i:2*i])*1.0+hammingdst(a[1*i:2*i],a[2*i:3*i])+hammingdst(a[2*i:3*i],a[3*i:4*i]))/i))

    for i in sorted(opts,key=lambda x: x[1])[:]:
        s=''
        print i
        splits = [a[j::i[0]] for j in range(i[0])]
        for k in splits:
            s+=chr(solve3(k.encode('hex'),5)[0][0])
        
        print 'key: {}'.format(s)
        
        print xor(a.encode('hex'),s.encode('hex')).decode('hex')
        raw_input('..')

#7
def solve7():
    
    enc = AES.new('YELLOW SUBMARINE',AES.MODE_ECB)
    print enc.decrypt(urllib.urlopen(r'http://cryptopals.com/static/challenge-data/7.txt').read().decode('base64'))

#8

def isecbforsure(data):
    blocks = {}
    for j in range(0,len(data),16):
        currentblock = data[j:j+16]
        if currentblock in blocks:
            blocks[currentblock]+=1
        else:
            blocks[currentblock]=1
            
    if len(set(blocks.values()))>1:
        return 1
    return 0

def solve8():
    a=urllib.urlopen(r'http://cryptopals.com/static/challenge-data/8.txt').read().split('\n')
    for i in a:
        if isecbforsure(i):
            print i

#9
def pad(string,length,char):
    return string+char*(length-len(string)%length)

#10
def mycbcenc(st,iv,key='YELLOW SUBMARINE'):
        res=''
        st = pkcs7pad(st)
        enc = AES.new(key,AES.MODE_ECB)
        for i in range(0,len(st),16):
             
            iv = enc.encrypt(x0r(st[i:i+16],iv))
            res+=iv
        return res
    
def mycbcdec(st,iv,key='YELLOW SUBMARINE'):
        res=''
        for i in range(0,len(st),16):
            
            enc = AES.new(key,AES.MODE_ECB)
            if i!=0:
                iv = x0r(enc.decrypt(st[i:i+16]),st[i-16:i])
            else:
                iv = x0r(enc.decrypt(st[i:i+16]),iv)
            
            res += iv
        return res
    
def solve10():
    a=urllib.urlopen(r'http://cryptopals.com/static/challenge-data/10.txt').read().decode('base64')
    print mycbcdec(a,'\x00'*16)

#11
def genkey(l):
    return ''.join(random.choice(string.hexdigits) for i in range(l))

def randomenc(data):
    startbytes = random.randint(5,10)
    endbytes = random.randint(5,10)
    state=random.randint(0,1)
    newdata = genkey(startbytes)+data+genkey(endbytes)
    if state:
        enc = AES.new(genkey(16),AES.MODE_ECB)
        
    else:
        enc = AES.new(genkey(16),AES.MODE_CBC,genkey(16))
    
    return enc.encrypt(newdata+genkey(16-len(newdata)%16))   
    
def decidetype1(func,targets):
    ecb=0
    cbc=0
    for i in targets:
        if isecbforsure(func(i)):
            ecb+=1
        else:
            cbc+=1
    print 'ecb: {}, notecb: {}'.format(ecb,cbc)

#12
def solve12():
    A_KEY = genkey(16)
    stuff = 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'.decode('base64')
    def sortarandomecbenc(data):
        newdata=data+stuff
        enc = AES.new(A_KEY,AES.MODE_ECB)
        return enc.encrypt(newdata+genkey(16-len(newdata)%16))  

    c=0
    first=len(sortarandomecbenc(''))
    while len(sortarandomecbenc('a'*c))==len(sortarandomecbenc('a'*(c+1))):
        c+=1
    d=c
    c+=1
    while len(sortarandomecbenc('a'*c))==len(sortarandomecbenc('a'*(c+1))):
        c+=1
    blocksize=c-d
    print 'blocksize: {}'.format(blocksize)
    print decidetype1(sortarandomecbenc,['a'*500 for i in range(100)])

    current=[]

    for currentblock in range(first/blocksize):
        print currentblock
        for i in range(blocksize-1,-1,-1):
            
            init = 'a'*i
            

            almostblock = sortarandomecbenc(init)[blocksize*currentblock:blocksize*(1+currentblock)]
            print blocksize*currentblock,blocksize*(1+currentblock)
            for j in string.printable:
                
                nice = init+''.join(current)+j
                
                if sortarandomecbenc(nice)[blocksize*currentblock:blocksize*(1+currentblock)]==almostblock:
                    print j,
                    current.append(j)
                    break
        print

    print ''.join(current)

#13
def solve13():
    def kvparse(st):
        cool = st.split('&')
        d = {}
        for i in cool:
            b = i.replace('&','').split('=')
            d[b[0]] = b[1].replace('=','')
        return d
    def profile(mail):
        return kvparse('email={}&uid={}&role=user'.format(mail,random.randint(1,999999999)))
        
    KEY13 = genkey(16)
    def enc13(profile):
        enc = AES.new(KEY13,AES.MODE_ECB)
        return enc.encrypt(profile+'\x00'*(16-(len(profile)%16)))

    def dec13(c):
        enc = AES.new(KEY13,AES.MODE_ECB)
        print enc.decrypt(c)
        return kvparse(enc.decrypt(c))

    lol = enc13('email={}&uid=1&role=user'.format('\x00'*10+'=1234&role=admin'*16))
    if (lol[16:32] == lol[32:48]):
        print 'lastblock with admin: {}'.format([lol[16:32]])
        goodlastblock = lol[16:32]
        nice = enc13('email=foo{}@bar.com&uid=10&role=user'.format('a'*11)) #"email=foo{}@bar.com&uid" should be multiple of 16 in length so uid fits with our crafted last block's = sign
        print dec13(nice[:-16]+goodlastblock)
    

#15

def pkcs7(st):
    padding = st[-1]
    if ord(padding)*padding == st[-ord(padding):] and st[-ord(padding)-1]!=padding:
        return st[:-ord(padding)]
    else:
        raise Exception('INVALID PADDING OR WUT')
#14
##bring from @home

#16

def solve16():
    KEY16=genkey(16)
    def pre16(st):
        
        return mycbcenc("comment1=cooking%20MCs;userdata="+st.replace(';','').replace('=','')+";comment2=%20like%20a%20pound%20of%20bacon",'\x00'*16,KEY16)

    def post16(st):
        return ';admin=true;' in mycbcdec(st,'\x00'*16,KEY16)
    dat = ':admin<true:'
    print 'userdata: {}'.format(dat)
    z=pre16(dat)
    print z
    print 'flipping bits 0,6,11 in block3...'
    q = z[:16]+x0r(z[16],'\x01')+z[17:22]+x0r(z[22],'\x01')+z[23:27]+x0r(z[27],'\x01')+z[28:]
    print post16(q),[mycbcdec(q,'\x00'*16,KEY16)]

#17
KEY17 = genkey(16)

def x0r(st1,st2):
    return ''.join([chr(ord(st1[i]) ^ ord(st2[i%len(st2)])) for i in range(len(st1))])
def pkcs7pad(st):
    a = (16 - len(st)%16) % 16
    return st+(a)*chr(a)

def f1():
    opts = ['MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=',
'MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=',
'MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==',
'MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==',
'MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl',
'MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==',
'MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==',
'MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=',
'MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=',
'MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93']
    c = pkcs7pad(random.choice(opts).decode('base64'))
    
    iv = genkey(16)
    enc=AES.new(KEY17,AES.MODE_CBC,iv)
    res = enc.encrypt(c)
    return res,iv

def f2(st,iv):
    enc=AES.new(KEY17,AES.MODE_CBC,iv)
    b = enc.decrypt(st)
    if pkcs7(b):
        return True
    return False

def solve17():
    fin=''
    r=''
    b=f1()


    a=(b[1]+b[0],b[1])
    while len(a[0])>=32:
        
        for k in range(1,17):    
            
            for i in range(256):
                guess=chr(i)
                try:
                    f2(a[0][:16-k]+x0r(a[0][16-k],x0r(guess,chr(k)))+x0r(x0r(r,a[0][16-k+1:]),chr(k))+a[0][16:32],a[1])
                    #print guess
                    r=guess+r
                except:
                    pass
        #print r
        fin+=r
        r=''
        a=(a[0][16:],a[1])
        
    return fin

#18
def myctr(st,key,nonce):
    enc = AES.new(key,AES.MODE_ECB)
    c = 0
    res = ''
    
    while c<len(st):
        noncest = '\x00'*8+struct.pack('<Q',nonce)
        stream = enc.encrypt(noncest)
        for i in range(16):
            #print c
            if c==len(st):
                break
            res+=x0r(st[c],stream[i])
            c+=1
        nonce+=1
    return res

#19
KEY19=genkey(16)
a=open(r'C:\users\team2\desktop\cryptopals\319.stuff','r').read().split('\n')
ciphers = map(lambda x: myctr(x.decode('base64'),KEY19,0),a)
z = [x0r(ciphers[-2],  i) for i in ciphers]
#' ice ', 19[1:], good match

def parse(stuff):
	return [i for i in [stuff[i:i+16] for i in range(0,len(stuff),16)]]


