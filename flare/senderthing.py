import string
import itertools
import subprocess

targets = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
prefix = ''

z = itertools.combinations_with_replacement(targets,3)

for i in z:
    t = prefix + ''.join(i)
    
    f = open(r'D:\flareon\5\key.txt','w')
    f.write(t)
    f.close()
    
    subprocess.Popen([r'D:\flareon\5\sender.exe',r'D:\flareon\5\key.txt'])
    
    
