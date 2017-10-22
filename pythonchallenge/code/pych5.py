import urllib
import urltest
import pickle
a=urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
smthin=pickle.loads(a)
for i in smthin:
	print ''.join(j[0]*j[1] for j in i)
