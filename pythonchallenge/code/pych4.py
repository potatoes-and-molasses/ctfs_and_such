import urltest
from urllib import *
a=urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345').read()
while 1:
    print a
    if 'nothing is ' in a:
        b=a[a.find('nothing is ')+len('nothing is '):]
    if 'Divide by two' in a:
        b=str(int(b)/2)
    print b
    a=urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(b)).read()
    
#after a year.. peak.html
