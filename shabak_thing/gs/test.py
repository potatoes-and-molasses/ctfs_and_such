from ctypes import*
import thread
import subprocess
import win32pipe, win32file
import os
import time
import string
import itertools
inp = 'ice cold'
p = win32pipe.CreateNamedPipe(r'\\.\pipe\flumbus_channel',
        win32pipe.PIPE_ACCESS_DUPLEX,
        win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT,
        1, 65536, 65536,300,None)

win32pipe.ConnectNamedPipe(p,None)
print win32file.ReadFile(p,4096)

win32file.WriteFile(p,inp)
print 'sent {}'.format(inp)
time.sleep(0.3)
print win32file.ReadFile(p,4096)
p.Close()
