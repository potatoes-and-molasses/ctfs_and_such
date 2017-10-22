import xmlrpclib
a=xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print a.system.listMethods()
print a.phone('Bert')
