import socket

def sendp(cmd):
        
	packet = 'CMD: \x01\x01\x01'+chr(len(cmd))+cmd
	a=socket.socket()
	a.connect(('34.215.112.21',5966))
	print 'sending command: '+cmd
	print a.send(packet)
	print a.recv(1024)
	print '--'
	print a.recv(1024)






