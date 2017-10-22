import bz2
from PIL import Image
import numpy
import cv2
a=Image.open(r'C:\users\team2\desktop\pych\zigzag.gif')
p=a.palette.getdata()[1][::3]
test=a.tostring()
test2=[p[ord(test[i])] for i in range(len(test))]
tesst=''.join(test2)
cool=''
coords=[]
for i in range(len(test[1:])):
    if test[i+1]!=tesst[i]:
        coords+=[(i/320,i%270)]
        cool+= test[i+1]

res= bz2.BZ2Decompressor().decompress(cool)
new=numpy.zeros((320,270,3),numpy.uint8)
for i in coords:

	for k in range(3):
		new[i[0]][i[1]][k]=255

cv2.imshow('ok',new)
cv2.waitKey(0)
cv2.destroyAllWindows()

s=set(res.split(' '))

#user=repeat,pass=switch(both r the only non-python keywords in s..
