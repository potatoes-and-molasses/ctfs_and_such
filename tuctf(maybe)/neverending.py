import socket
import string
a=socket.socket()
a.connect(('146.148.102.236',24069))
mors = {'..-.': 'F', '-..-': 'X',
                 '.--.': 'P', '-': 'T', '..---': '2',
                 '....-': '4', '-----': '0', '--...': '7',
                 '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                 '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                 '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                 '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                 '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                 '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}
dr = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

opts = set(["my luckdragon",'reading is dangerours', 'save the princess', 'the oracle', 'welcome atreyu', 'i owe you', 'the nothing', 'gmorks cool', 'dont forget auryn', 'fragmentation', 'try swimming', 'moon child', 'atreyu vs gmork', 'bastian', 'giant turtle'])
coolopts = {(7, 2, 10):"reading is dangerours",
(4, 3, 8):"save the princess",
(3, 6):"the oracle",
(7, 6):"welcome atreyu",
(1, 3, 3):"i owe you",
(3, 7):"the nothing",
(6, 4):"gmorks cool",
(4, 6, 5):"dont forget auryn",
(13,):"fragmentation",
(3, 8):"try swimming",
(4, 5):"moon child",
(6, 2, 5):"atreyu vs gmork",
(7,):"bastian",
(5, 6):"giant turtle",
(2,10):"my luckdragon"}
def mapopt(opt):
	return tuple([len(i) for i in opt.split(' ')])
def repeats(st):
	allstuff=[]
	for i in (st):
		c=0
		temp=st
		cool=[]
		while temp.find(i)!=-1:
			c+=1
			cool.append(temp.find(i))
			temp = temp[temp.find(i)+1:]

		allstuff.append((c,tuple(cool)))
	return tuple(allstuff)
ddd={}
for i in opts:
	ddd[repeats(i)]=i
def shift(n,st):
    return ''.join(dr[(dr.find(i)+n)%len(dr)] for i in st)

for i in range(50):
    print a.recv(4096)
    a.send('abcd\n')
    z=a.recv(4096)
    words = (z[z.find('What is')+8:z.find('decr')-2]).split('   ')
    res=[]
    for i in words:
        res.append(''.join(mors[j] for j in i.split(' ')))
    print ' '.join(res)
    
    a.send(' '.join(res)+'\n')
print a.recv(4096)
print '--'
for i in range(50):
    a.send('aabc'+'\n')
    z = a.recv(8192)
    print z
    diff = ord(z[18])-ord(z[0])
    stuff = z[z.find('What is ')+8:z.find('decrypted')-1]
    res = shift(-13,stuff)
    print res
    a.send(res+'\n')
    opts.add(res)
    z = a.recv(8192)
    print z

print '--'

for i in range(50):
    a.send('abcd'+'\n')
    z = a.recv(8192)
    print z
    stuff = z[z.find('What is ')+8:z.find('decrypted')-1]
    res = coolopts[mapopt(stuff)]
    a.send(res+'\n')
        
    z = a.recv(8192)
    print z

print '--'
for i in range(50):
    a.send('aabc'+'\n')
    z = a.recv(8192)
    print z
    diff = ord(z[18])-ord(z[0])
    stuff = z[z.find('What is ')+8:z.find('decrypted')-1]
    res = shift(-diff,stuff)
    print res
    a.send(res+'\n')
    opts.add(res)
    z = a.recv(8192)
    print z
print '--'
for i in range(50):
    a.send('abcd'+'\n')
    z = a.recv(8192)
    print z
    stuff = z[z.find('What is ')+8:z.find('decrypted')-1].replace('\x7f',' ')
    res = coolopts[mapopt(stuff)]
    a.send(res+'\n')
        
    z = a.recv(8192)
    print z
    
print '--'
for i in range(50):
    a.send('aaaaabcda'+'\n')
    z = a.recv(8192)
    print z
    stuff = z[z.find('What is ')+8:z.find('decrypted')-1]
    res = ddd[repeats(stuff)]
    a.send(res+'\n')
        
    z = a.recv(8192)
    print z
    
print '--'
for i in range(50):
    a.send('aaaaabcda'+'\n')
    z = a.recv(8192)
    print z
    diff1 = ord(z[23])-ord(z[0])
    diff2 = ord(z[24])-ord(z[1])
    diff3 = ord(z[25])-ord(z[2])
    diffs=[diff1,diff2,diff3]
    stuff = z[z.find('What is ')+8:z.find('decrypted')-1]
    stuff = ''.join(shift((-diffs[i%3]),stuff[i]) for i in range(len(stuff)))#no need to even solve.. just synch diffs.. but w.e
    try:
        res = ddd[repeats(stuff)]
    except:
        res=stuff
    a.send(res+'\n')
        
    z = a.recv(8192)
    print z

print '--'
for i in range(50):
    a.send('abcd'+'\n')
    z = a.recv(8192)
    print z
    stuff = z[z.find('What is ')+8:z.find('decrypted')-1].replace('\x00','')
    res = coolopts[mapopt(stuff)]
    a.send(res+'\n')
        
    z = a.recv(8192)
    print z
