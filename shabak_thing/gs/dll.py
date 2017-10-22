from ctypes import*
import thread
import subprocess
import win32pipe, win32file
import os
import time
import string
import itertools
def func():
    #si = subprocess.STARTUPINFO()
    #si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    f=open(r'C:\users\team2\desktop\gs\output.log','w')
    f.write(subprocess.check_output(r'C:\Users\Team2\Documents\Visual Studio 2010\Projects\gs\Debug\gs.exe',creationflags=0x08000000))
    f.close()
    

def trystuff(inp):
    thread.start_new_thread(func,())

    p = win32pipe.CreateNamedPipe(r'\\.\pipe\flumbus_channel',
        win32pipe.PIPE_ACCESS_DUPLEX,
        win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT,
        1, 65536, 65536,300,None)

    win32pipe.ConnectNamedPipe(p,None)
    #print win32file.ReadFile(p,4096)
    
    win32file.WriteFile(p,inp)
    #print 'sent {}'.format(inp)
    #print win32file.ReadFile(p,4096)
    p.Close()
    time.sleep(0.05)
    f=open(r'C:\users\team2\desktop\gs\output.log','r')
    val = f.read()
    f.close()
    
    os.remove(r'C:\users\team2\desktop\gs\output.log')
    return val
##base=string.ascii_lowercase
##nope='Oh Man, you need to work on work music skillz, Wubba Lubba Dub Dub!!!\r\n'
##for i in range(8,1,-1):
##    print i
##    opts = itertools.product(base,repeat=i)
##    for j in opts:
##        q = ''.join(j)
##        res = trystuff(q)
##        if res==nope:
##            continue
##        else:
##            temp = res
##            print j
            
