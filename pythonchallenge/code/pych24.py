import cv2

a=cv2.imread(r'C:\users\team2\desktop\pych\24.png')

visited=set([])

steps=[(1,0),(0,1),(-1,0),(0,-1)]

class Link():
    def __init__(self,value,pre):
        self.value=value
        self.pre=pre

q=[((0,639),Link((0,639),None))]
c=0
while q:
    c+=1
    current = q.pop(0)
    if current[0][0]>640 or current[0][0]<0 or current[0][1]>640 or current[0][1]<0 or current[0] in visited:
        continue
    elif sum(a[current[0][0]][current[0][1]])==765:
        continue
    elif current[0]==(640,1):
        print 'done'
        break
    visited.add(current[0])
    for i in steps:
        q.append(((current[0][0]+i[0],current[0][1]+i[1]),Link((current[0][0]+i[0],current[0][1]+i[1]),current[1])))

#who needs linked lists when you can do pretty -> symbols in strings!

stuff = []
current=current[1]
while current.pre:
    stuff.append(current.value)
    current=current.pre
        
st=''
for i in stuff[::-1]:
    st+=chr(a[i[0]][i[1]][2])
    a[i[0]][i[1]][0]=255
st=st[::2]

f=open(r'C:\users\team2\desktop\pych\solved.zip','wb')
f.write(st)
f.close()


