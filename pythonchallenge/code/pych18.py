import urllib
import cv2
import difflib
##a=urllib.urlopen(r'http://www.pythonchallenge.com/pc/return/balloons.jpg').read()
##f=open(r'C:\users\team2\desktop\pych\balloons.jpg','wb')
##f.write(a)
##f.close()

b=cv2.imread(r'C:\users\team2\desktop\pych\balloons.jpg')
right=b[::,len(b[0])/2::,::]
left=b[::,:len(b[0])/2:,::] 
cv2.imshow('ok',left-right)
cv2.waitKey(0)
cv2.destroyAllWindows()
#guess not...
#urllib.urlopen('http://www.pythonchallenge.com/pc/return/brightness.html').read()

#downloaded deltas.gz

delta = open(r'C:\users\team2\desktop\pych\delta.txt','rb').read()
delta=delta.split('\n')
a=difflib.Differ()

l=[i[:53] for i in delta]
r=[i[56:] for i in delta]
things=[i for i in a.compare(l,r)]
one=[i[2:] for i in things if i[0]=='+']
two=[i[2:] for i in things if i[0]=='-']
three=[i[2:] for i in things if i[0]==' ']
c=0
for lol in [one,two,three]:
    data=''.join(map(lambda x: ''.join(chr(int(i,16)) for i in x.split(' ')),filter(lambda x: x!='',[i.strip(' ') for i in lol])))
    f=open(r'C:\users\team2\desktop\pych\18-{}.png'.format(c),'wb')
    c+=1
    f.write(data)
    f.close()
#pictures=butter,fly(un/pw),hex/bin.html(at /pc)
