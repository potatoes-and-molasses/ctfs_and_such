import urllib
#evil4.jpg  = Bert is evil! go back!
a=urllib.urlopen(r'http://www.pythonchallenge.com/pc/return/evil2.gfx').read()

files=[a[i::5] for i in range(5)]
for i,j in enumerate(['jpg1.jpg','png1.png','gif1.gif','png2.png','jpg2.jpg']):
    f=open(r'C:\users\team2\desktop\pych\{}'.format(j),'wb')
    f.write(files[i])
    f.close()

#disproportional
    
