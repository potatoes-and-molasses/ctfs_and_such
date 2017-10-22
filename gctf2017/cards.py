import socket,random

a=socket.socket()
a.connect(('anon.ctfcompetition.com',1337))
print a.recv(4096)
print a.recv(4096)

a.send('newacc\n'*64)
print a.recv(1048576)
print a.recv(1048576)
a.send('newcard\n'*65)
print a.recv(1048576)
print a.recv(1048576)

tosend=''
for i in range(1,65):
    tosend+='assoc ucard{} uaccount{}\nassoc ucard{} uaccount{}\nassoc ccard{} uaccount{}\n'.format(hex(i),hex(i),hex(i+1),hex(i),hex(i),hex(i))

a.send(tosend)
print a.recv(1048576)
print a.recv(1048576)








a.send('backup\n')
data = ''
while 'burnt?' not in data:
    data += a.recv(1048576)
    print 1




q = 't = '+data.replace('\n','').replace('\r','').replace('So, which cards are burnt?Answer with a string of zeroes and ones, no spaces.','')
exec q
d ={}
for i in t:
    if i['account'] not in d:
        d[i['account']] = i['cards']
    else:
        d[i['account']] += i['cards']

gaccs = filter(lambda x: len(d[x])==3,d)
cards = {}
for i in t:
    for j in i['cards']:
        if j['card'] not in cards:
            cards[j['card']] = [i['account']]
        else:
            cards[j['card']] += [i['account']]


def findnextacc(acc,prevacc=''):
    for card in d[acc]:
        for nextacc in cards[card['card']]:
            if acc!=nextacc and nextacc!=prevacc:
                if nextacc in gaccs:
                    return nextacc
    return '||end of chain'

acc = gaccs[random.randint(0,len(gaccs)-1)]
def dothings(acc):
    answer= ''
    prevacc=''
    res=''
    chain=[]
    while acc!='||end of chain':
        prevacc,acc = acc,findnextacc(acc,prevacc)
        chain+=[prevacc]
        print '{}->{}'.format(prevacc,acc)
    chain = chain[::-1]
    acc = chain[-1]
    prevacc = chain[-2]
    chain = chain[:-1]
    while acc!='||end of chain':
        prevacc,acc = acc,findnextacc(acc,prevacc)
        chain+=[prevacc]
        print '{}->{}'.format(prevacc,acc)
    print 'total chain length: {}'.format(len(chain))
    if(len(chain)!=64):
        print 'choosing a new contender'
        return dothings(gaccs[random.randint(0,len(gaccs)-1)])
    

    for i in chain:
            if 'flagged' in d[i][0] or 'flagged' in d[i][1] or 'flagged' in d[i][2]:
                    answer+='1'
            else:
                    answer+='0'
    print answer
    a.send('{}\n'.format(answer))
    print a.recv(65536)
dothings(acc)
