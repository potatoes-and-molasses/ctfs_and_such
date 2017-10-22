p = 174807157365465092731323561678522236549173502913317875393564963123330281052524687450754910240009920154525635325209526987433833785499384204819179549544106498491589834195860008906875039418684191252537604123129659746721614402346449135195832955793815709136053198207712511838753919608894095907732099313139446299843

g = 41899070570517490692126143234857256603477072005476801644745865627893958675820606802876173648371028044404957307185876963051595214534530501331532626624926034521316281025445575243636197258111995884364277423716373007329751928366973332463469104730271236078593527144954324116802080620822212777139186990364810367977

import random
from hashlib import sha256
import socket
import time
import Crypto.Random 
from Crypto.Cipher import AES
BLOCK_SIZE = 16
R = Crypto.Random.new()
primes = [int(i) for i in open(r'C:\users\team2\desktop\primes.txt').read().split(',')]
def pad(m):
    o = BLOCK_SIZE - len(m) % BLOCK_SIZE
    return m + o * chr(o)

def unpad(p):
    return p[0:-ord(p[-1])]
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)
def send_encrypted(KEY, m):
    IV = R.read(BLOCK_SIZE)
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    c = aes.encrypt(pad(m))
    return (IV + c).encode('hex')

def read_encrypted(KEY,dat):
    data = dat
    IV, data = data[:BLOCK_SIZE], data[BLOCK_SIZE:]
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    m = unpad(aes.decrypt(data))
    return m
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
##b = random.randint(1, 2**46)
##B = pow(g,b,p)
##s = socket.socket()
##s.connect(('shell2017.picoctf.com',40209))
##data = s.recv(4096)
##data = s.recv(4096)
##astart = data.find('A = ')+4
##A = int(data[astart:data.find('\n',astart)])
##print "B = {}".format(B)
##time.sleep(1)
##s.send('{}\n'.format(B))
##time.sleep(1)
##K = pow(A, b, p)
##KEY = sha256(str(K)).digest()
##
##s.send(send_encrypted(KEY,raw_input('password:'))+'\n')
##print 'sentall'
##time.sleep(1)
##print s.recv(4096)
##
##
table = {}
S = 0

A=60599224471338675280892530751916349778515159413752423808328059701102187627870714718035966693602191072973114841123646111608872779841184094624255525186079109811898831481367089940015561846391171130215542875940992971840860585330764274682844976540740482087538338803018712681621346835893113300860496747212230173641
B=41577936475113646062415839313533664222336390873095585592257233546410748309845182921273101711259044469844745154398797450729717767422505327649336923087518273833440859523881791932947163012973287757609314935398468435619627316484481259644562078527117416504710807415325721826304371028711933641605633408713301811494

for i in range(0, 2**33, 2**20): 
   table[pow(g, i, p)] = i



for i in range(0, 2**18):
   B = (B * g) % p
   if B in table:
       print  ' >> B = g ^', table[B] - i
       S = pow(A, table[B] - i, p)
       break

print 'found:\n\n', S, '\n'
