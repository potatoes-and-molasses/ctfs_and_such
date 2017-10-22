import socket
a = socket.socket()
a.connect(('shell2017.picoctf.com',61161))
b = ''
c= ''
while '8/8' not in c:
    c = a.recv(1000000)
    b+=c
    raw_input('.')
f = open(r'C:\users\team2\desktop\pico2017\worldchat','w')
f.writelines(b)
f.close()
