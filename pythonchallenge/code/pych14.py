#comment - remember: 100*100 = (100+99+99+98) + (...
#maybe they mean (100+99+99+98) + (98+97+97+96) + (..., which is true
#end result is a cat(cat.html,name=uzi)


import cv2
import urllib
import numpy
a=urllib.urlopen('http://www.pythonchallenge.com/pc/return/wire.png').read()

f=open(r'C:\users\team2\desktop\pych\wire.png','wb')
f.write(a)
f.close()


b=cv2.imread(r'C:\users\team2\desktop\pych\wire.png')
new = numpy.zeros((100,100,3),numpy.uint8)

def spiral(l):
    x=-1
    y=dy=0
    dx=1
    steps=0
    cool=[[i+1,i,i,i-1] for i in range(l-1,-1,-2)]
    
    current=[]
    loc=0
    for i in cool:
        current+=i
    
    for i in range(l**2):
        
        x,y=x+dx,y+dy
        steps+=1
        yield x,y
        
        
        
        if steps==current[loc]:
            loc+=1
            steps=0
            
            dx,dy=-dy,dx
            
coolsome=spiral(100)

c=0
for i in coolsome:
    new[i[0]][i[1]]=b[0][c]
    c+=1

cv2.imshow('ok',new)
cv2.waitKey(0)
cv2.destroyAllWindows()
        
