###!/usr/bin/env python
##
def xor(s1, s2):
    res = [chr(0)]*12
    for i in range(len(res)):
        q = ord(s1[i])
        d = ord(s2[i])
        k = q ^ d
        res[i] = chr(k)
    res = ''.join(res)
    return res

##def add_pad(msg):
##    l = 12 - len(msg)%12
##    msg += chr(l)*l
##    return msg
##
##with open('flag.png') as f:
##    data = f.read()
##
##data = add_pad(data)
##
##with open('key') as f:
##    key = f.read()
##
##enc_data = ''
##for i in range(0, len(data), 12):
##    enc = xor(data[i:i+12], key)
##    enc_data += enc
##
##with open('encrypted.png', 'wb') as f:
##    f.write(enc_data)


def engfreq(st,notprintablesig=5):
    return 1.0*(len(filter(lambda x: x in string.ascii_letters,st))-notprintablesig*len(filter(lambda x: x not in string.printable,st)))/len(st)#the -5

def solve3(a='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736',freq=5):
    
    opts = []
    for i in range(256):
        opts.append((i,engfreq(xor(a,chr(i)),freq)))
    best = max(opts, key=lambda x: x[1])
    
    return best,xor(a,chr(best[0]))
a=open(r'C:\users\team2\desktop\ascii\encrypted.png','rb').read()
def x0r(st1,st2):
    return ''.join([chr(ord(st1[i]) ^ ord(st2[i%len(st2)])) for i in range(len(st1))])
z = open(r'C:\users\team2\desktop\oxygen.png','rb').read()
key = x0r(z[:12],a[:12])
t = open(r'C:\users\team2\desktop\ascii\new.png','wb')
t.write(x0r(a,key))
t.close()
