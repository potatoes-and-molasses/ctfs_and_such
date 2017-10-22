import httplib
import binascii
import re
auth=binascii.b2a_base64('butter:fly').replace('\n','')





r1,r2=30203,2123456789

while 1:
    print r1
    a=httplib.HTTPConnection('www.pythonchallenge.com')
    a.request('GET','/pc/hex/unreal.jpg',headers={'Authorization':'Basic {}'.format(auth),'Range':'bytes={}-{}'.format(r1,r2)})
    b=a.getresponse()
    if b.status==206:
        print '{}-{}'.format(r1,r2)
        data = b.read()
        print data
        r1=re.search(r'-(.*)/',b.getheader('Content-Range')).group(1)
    else:
        r1=str(int(r1)+1)
    if data[:2]=='ok':
        break
r1,r2=2123456789,2223456789

a=httplib.HTTPConnection('www.pythonchallenge.com')
a.request('GET','/pc/hex/unreal.jpg',headers={'Authorization':'Basic {}'.format(auth),'Range':'bytes={}-{}'.format(r1,r2)})
b=a.getresponse()
if b.status==206:
    print '{}-{}'.format(r1,r2)
    print b.read()
    r1=re.search(r'-(.*)/',b.getheader('Content-Range')).group(1)

r1,r2=2123456744,2123456788

while 1:
    a=httplib.HTTPConnection('www.pythonchallenge.com')
    a.request('GET','/pc/hex/unreal.jpg',headers={'Authorization':'Basic {}'.format(auth),'Range':'bytes={}-{}'.format(r1,r2)})
    b=a.getresponse()
    print r1
    if b.status==206:
        print '{}-{}'.format(r1,r2)
        print b.read()
        r1-=1


r1=1152983631
a=httplib.HTTPConnection('www.pythonchallenge.com')
a.request('GET','/pc/hex/unreal.jpg',headers={'Authorization':'Basic {}'.format(auth),'Range':'bytes={}-{}'.format(r1,r2)})
b=a.getresponse()
z=b.read()
f=open(r'C:\users\team2\desktop\pych\20.zip','wb')
f.write(z)
f.close()


