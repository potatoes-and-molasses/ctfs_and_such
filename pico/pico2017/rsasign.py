import socket
import time
sleep1=0.1
sleep2=0.2
primes_c = 120
primes = [int(i) for i in open(r'primes.txt').read().split(',')]

a=socket.socket()
a.connect(('shell2017.picoctf.com',27525))
data = a.recv(2048)
data2 = a.recv(2048)
n = int(data2[4:data2.find('\n',1)])
e = 65537
start = time.time()
psigned = {}
for i in primes[:primes_c]:
    print 'signing {}...'.format(i)
    time.sleep(sleep1)
    a.send('{}\n'.format(i))
    time.sleep(sleep2)
    signature = a.recv(2048)
    
    sig = int(signature[11:signature.find('\n')])
    psigned[i]=sig
    print 'done!'
a.send('-1\n')
time.sleep(sleep2)
data = a.recv(2048)
print data
pcount = {i:0 for i in psigned}
challenge = int(data[11:data.find('\n')])
for i in psigned:
    while not challenge%i:
        pcount[i]+=1
        challenge /= i
if challenge == 1:
    print 'success!'
    print pcount
    res = 1
    for i in psigned:
        for j in range(0,pcount[i]):
            res = (res * psigned[i]) % n
    a.send('{}\n'.format(res))
    sleep(sleep2)
    print a.recv(2048)
    print a.recv(2048)
else:
    print 'left unfactored:'
    print challenge
    print pcount
end = time.time()

print 'time: {}'.format(end-start)
        





