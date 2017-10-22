import zipfile
import itertools
import string
import cv2
##st = string.digits+string.ascii_letters+'_'
##a=zipfile.ZipFile(r'C:\users\team2\desktop\prag\problem.zip')
##z=0
##for pre in ['j0hn','J0hn','j0hny','','J0hny']:
##    for j in range(1,5):
##        print pre+str(j)
##        for i in itertools.combinations(st,j):
##            
##            try:
##                z=a.extractall(path=r'C:\users\team2\desktop\prag',pwd=pre+''.join(i))
##                pw=''.join(i)
##
##            except:
##                pw=0
##                
##            if z:
##                print ''.join(i)
##                break
##        if z:
##            break
##    if z:
##        break
##
##
##        
a=cv2.imread(r'C:\users\team2\downloads\image.png')
def datafrompixel(px):
    return ((px[0]&3)<<2) + (px[1]&3),px[2]&1
steganSymbolArray = []
steganSymbolArray.append({'runlength':3,'value':1})
steganSymbolArray.append({'runlength':2,'value':0})
steganSymbolArray.append({'runlength':5,'value':1})
steganSymbolArray.append({'runlength':1,'value':0})
steganSymbolArray.append({'runlength':1,'value':1})
steganSymbolArray.append({'runlength':2,'value':0})
steganSymbolArray.append({'runlength':2,'value':1})
steganSymbolArray.append({'runlength':2,'value':0})
steganSymbolArray.append({'runlength':1,'value':1})
steganSymbolArray.append({'runlength':1,'value':0})
steganSymbolArray.append({'runlength':3,'value':1})
steganSymbolArray.append({'runlength':2,'value':0})
steganSymbolArray.append({'runlength':5,'value':1})
steganSymbolArray.append({'runlength':4,'value':0})
steganSymbolArray.append({'runlength':3,'value':1})
steganSymbolArray.append({'runlength':1,'value':0})
steganSymbolArray.append({'runlength':3,'value':1})
steganSymbolArray.append({'runlength':1,'value':0})
