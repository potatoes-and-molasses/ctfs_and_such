import bz2
import zlib

temp=open(r'C:\users\team2\desktop\pych\package.pack','rb').read()
log=''
while 1:
    print [hex(ord(i)) for i in temp[:10]]
    print temp[:10]
    if temp[:2]=='BZ':
        log+='1'
        temp=bz2.BZ2Decompressor().decompress(temp)
    elif temp[:2]=='x\x9c':
        log+='0'
        temp=zlib.decompress(temp)
    elif temp[-1:-3:-1] in ['BZ','x\x9c']:
        log+='2'
        temp=temp[::-1]
    else:
        break
print temp
print log.replace('2','\n').replace('1','X').replace('0',' ')

