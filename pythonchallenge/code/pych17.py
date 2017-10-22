import urllib
import re
import bz2
data=''
cool=urllib.urlopen(r'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345')
filebytes=[]
while 'that\'s it' not in data:
    data=cool.read()
    print data
    cookie=cool.headers.getheader('set-cookie')
    print cookie
    filebytes+=[re.match(r'info=(.*?);',cookie).group(1)]
    cool=urllib.urlopen(r'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={}'.format(data[data.find('nothing is ')+len('nothing is '):]))
    
thing=''.join(map(lambda x: chr(int(x.replace('%',''),16)) if len(x)>1 else x,filebytes))
thing= thing.replace('+',' ',1)#first + is actually a ' ' that was url encoded.. second one is really a +(the horror!)
print bz2.BZ2Decompressor().decompress(thing)
#res = 'is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.'

#use pych13 to phone Leopold(mozart's father) - '555-VIOLIN' - url leads to http://www.pythonchallenge.com/pc/stuff/violin.php
#changed cookie to the flowers are on their way.
