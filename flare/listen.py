import socket
import re
import binascii
import thread
import subprocess
import time
import os

a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
prefix=''
a.bind(('127.0.0.1',80))
a.listen(10)
alll=''
res = 'UDYs1D7bNmdE1o3g5ms1V6RrYCVvODJF1DpxKTxAJ9xuZW=='
result = [res[i:i+4] for i in range(0,len(res),4)]
i=0

def func(towrite):
    time.sleep(2)
    os.chdir(r'D:\flareon\5')
    
    f = open(r'D:\flareon\5\key.txt','w')
    f.write(towrite)
    f.close()
        
    subprocess.Popen([r'D:\flareon\5\sender.exe'])

while 1:
    alll=''
    inp = raw_input('sh>')
    func(inp)
        
    while 1:
        
        #thread.start_new_thread(func,(1,))
        c,b = a.accept()

        data = c.recv(1024)

        #print data
        alll+=data
        c.send('''HTTP/1.0 200 OK
    Server: BaseHTTP/0.3 Python/2.7.9
    Date: Tue, 21 Jul 2015 21:13:43 GMT
    Content-type: text/html

    1''')


        
        #print ''.join(z)
        #print binascii.a2b_base64(''.join(z))
        z=re.findall(r'\r\n\r\n(.{4})',alll)
        #if z.group(1)==result[i]:
            #i+=1
            #alll+=z.group(1)
            #print alll
        print z
        extra = len(inp) % 3
        if extra:
            extra=1
        if(len(inp)/3 + extra == len(z)):
            break
        
    print result
a.close()

z=re.findall(r'\r\n\r\n(.{4})',alll)
print ''.join(z)
#print binascii.a2b_base64(''.join(z))

