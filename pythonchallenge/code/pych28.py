import cv2

a=cv2.imread(r'C:\users\team2\desktop\pych\bell.png')

green = a[::,::,1]
things=[[] for i in range(len(green))]
for j in range(len(things)):
	for i in range(0,len(green[0]),2):
		things[j]+=[green[j][i]-green[j][i+1]]


not21442=[]
for i in things:
	for j in i:
		if j not in [214,42]:
			not21442+=[j]

print ''.join(chr(i) if i <= ord('z') else chr(256-i) for i in not21442)
#whatnow?
