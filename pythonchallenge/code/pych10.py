import urllib

#print urllib.urlopen(r'http://www.pythonchallenge.com/pc/return/sequence.txt').read()
#(huge file from previous=user/pw)
#a = [1, 11, 21, 1211, 111221,
#len(a[30])?
def nextlol(st):
    things=''
    current=None
    count=0
    for i in st:
        if i==current:
            count+=1
        else:
            if current!=None:
                things+=str(count)+current
            current=i
            count=1
    
    things+=str(count)+current
    return things
i='1'
for j in range(30):
    i=nextlol(i)
print i
