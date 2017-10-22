import urllib
print urllib.urlopen('http://www.pythonchallenge.com/pc/hex/bonus.html').read()
for i in range(26):
	print ''.join([(chr(97+(ord(j)+i)%26)) if j.isalpha()
                       else j for j in 'va gur snpr bs jung?'])

#module=this.py, google much:D

	
