import md5
import urllib
import wave
import cv2
import numpy
##a=open(r'C:\users\team2\desktop\pych\mybroken.zip','rb').read()
##done=0
##for i in range(len(a)):
##	for j in range(256):
##		md=md5.new()
##		newzip=a[:i]+chr(j)+a[i+1:]
##		md.update(newzip)
##		if md.digest()=='\xbb\xb8\xb4\x99\xa0\xee\xf9\x9b\x52\xc7\xf1\x3f\x4e\x78\xc2\x4b':
##			print 'foundmatch: {} {}'.format(i,j)
##			done=1
##			break
##	if done:
##		break
###picture=speed, doesnt seem to help:/
##
##
##for i in range(1,26):
##    a=urllib.urlopen(r'http://www.pythonchallenge.com/pc/hex/lake{}.wav'.format(i)).read()
##    with open(r'C:\users\team2\desktop\pych\waves\{}.wav'.format(i),'wb') as f:
##        f.write(a)
##
##
##
##
new2 = numpy.zeros((300,300,3),numpy.uint8)
for n in range(25):
    a=wave.open(r'C:\users\team2\desktop\pych\waves\{}.wav'.format(n+1))
    t=a.getnframes()
    pixels=[]
    for i in range(t/3):
        pixels+=[a.readframes(3)]

    cool=iter(pixels)

    new = numpy.zeros((60,60,3),numpy.uint8)
    for i in new:
        for j in i:
            thing=cool.next()
            for k in range(3):
                j[k]=ord(thing[k])
    cv2.imwrite(r'C:\users\team2\desktop\pych\waves\{}.bmp'.format(n+1),new)
    new2[60*(n/5):60*(n/5+1),60*(n%5):60*(n%5+1)]=new
cv2.imshow('ok',new2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#picture=decent
