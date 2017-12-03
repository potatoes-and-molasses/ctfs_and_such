import math
import re
import itertools
##1 
##print sum(filter(lambda x: not x%3 or not x%5, range(1000)))

##2
def fib(upto):
    past, present = 0, 1
    future = past + present
    while future < upto:
        yield future
        past, present = present, future
        future= past + present
        
##sum(filter(lambda x: not x%2, fib(4000000)))        

##3
##n = 600851475143
##def factors(n):
##    factors = set([])
##    for i in range(1, int(n**0.5)+1):
##        if not n%i:
##            factors.add(i)
##    return factors
##print max(filter(lambda x: isp(x), factors(n)))

##4
##mx = 0
##for i in range(999, 100, -1):
##    for j in range(999, 100, -1):
##        n = str(i*j)
##        if n == n[::-1]:
##            mx = max(i*j, mx)
##print mx

##5
##(its given to us that 2520 fills the req. for 1..10)
##print 2520*11*13*2*17*19

##6
##sqsm = sum(i**2 for i in range(1,101))
##smsq = sum(i for i in range(1,101))**2
##print smsq-sqsm

##7

def isp(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if not n%i:
            return False
    return True
##i, c = 13, 6

##while True:
##    i += 1
##    if isp(i):
##        c+=1
##        if c == 10001:
##            print i
##            break

##8
##print 9*9*8*7*9 #(by looking at the 1k digits number for a minute)

##9
##f=0
##for i in range(400):
##    for j in range(400):
##        if i**2 + j**2 == (1000-i-j)**2:
##            print i*j*(1000-i-j)
##            f=1
##            break
##    if f == 1:
##        break

##10 using #7
##print sum(filter(lambda x: isp(x), range(2,2000000)))

##11
##print 89*94*97*87 # by coloring numbers higher than 80 in the chart and looking for 4-red straight sequences

##12
##def factors(n):
##    factors = set([])
##    for i in range(1, int(n**0.5)+1):
##        if not n%i:
##            factors.add(i)
##            factors.add(n/i)
##    
##    return factors
##i = 0
##while True:
##    i+=1
##    n = sum(range(i))
##    if len(factors(n)) > 500:
##        print n
##        break

##13
##print 5537376230
##(on my PC at home, copying 5,000 digits from a phone is bad)

##14
##results, res, mx = {}, 0, 0
##for i in range(1,1000000):
##    length = 1
##    current = i
##    while current!=1:
##
##        if current in results:
##            length += results[current]-1
##            current = 1
##        else:
##            length += 1
##            if current%2:
##                current = current*3+1
##                
##            else:
##                current = current/2
##                
##    results[i] = length
##    if length>mx:
##        mx, res = length, i
##print res, mx

##15
##results = {}
##def count(n1,n2):
##    if n1==0 or n2==0:
##        return 1
##    elif (n1,n2) not in results:
##        results[(n1,n2)] = count(n1, n2-1) + count(n1-1, n2)
##        results[(n2,n1)] = count(n1, n2-1) + count(n1-1, n2)
##    return results[(n1,n2)]
##print count(20,20)

##16
##n=2**1000
##s = sum(int(i) for i in str(n))
##print s

##17
##transition = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'\
##              , 100: 'hundred', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'\
##              ,11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
##AND = 3
##THOUSAND=11
##ltrs = THOUSAND
##HUNDRED=7
##
###1-20 by the dictionary
##for i in range(1,21): 
##    ltrs += len(transition[i])
##    
###splitting to two parts 20-100
##for i in range(21, 100):
##    ltrs += len(transition[i%10]+transition[int(i/10)*10])
##
###hundredand+(depending if between 11-19 or a regular number)
##for i in range(100, 1000):
##    ltrs += len(transition[int(i/100)])+HUNDRED
##    if i%100:
##        ltrs += AND
##        if 0<=i%100<11 or i%100>19:
##            ltrs += len(transition[int(i/10)%10*10]+transition[i%10])
##        else:
##            ltrs += len(transition[i%100])
##
##print ltrs
##
##class pyramid():
##    rows=[[]]
##    def __init__(self, height):
##        self.rows = [[range(i)] for i in range(height, 0, -1)]
##
##    def addlower(self, rownum):
##        for i in range(len(self.rows[rownum][0])):
##            print rownum, i, self.rows[rownum][0][i]
##            self.rows[rownum][0][i] += max(self.rows[rownum-1][0][i], self.rows[rownum-1][0][i+1])
##    def __repr__(self):
##        return '\n'.join(str(row) for row in self.rows)
##
##    def write_row(self, rownum):
##        for i in range(len(self.rows[rownum][0])):
##            self.rows[rownum][0][i] = input()
##
##    def write_all(self):
##        for i in range(len(self.rows)):
##            print 'row '+str(i)
##            self.write_row(i)
##
##    def add_all(self):
##        for i in range(1, len(self.rows)):
##            self.addlower(i)
####    def __init__(self, arr):
####        self.rows = arr
##
##a = pyramid(15)
##a.write_all()
##a.add_all()
##print a.rows[-1][0][0]

#[[[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]], [[125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54]], [[255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148]], [[325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233]], [[378, 317, 231, 321, 354, 372, 393, 354, 360, 293, 247]], [[419, 365, 393, 387, 419, 425, 430, 376, 454, 322]], [[460, 434, 419, 475, 508, 470, 510, 524, 487]], [[559, 499, 479, 536, 514, 526, 594, 616]], [[647, 501, 613, 609, 533, 657, 683]], [[666, 614, 636, 684, 660, 717]], [[686, 640, 766, 731, 782]], [[704, 801, 853, 792]], [[818, 900, 935]], [[995, 999]], [[1074]]]
##[[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
##[[125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54]]
##[[255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148]]
##[[325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233]]
##[[378, 317, 231, 321, 354, 372, 393, 354, 360, 293, 247]]
##[[419, 365, 393, 387, 419, 425, 430, 376, 454, 322]]
##[[460, 434, 419, 475, 508, 470, 510, 524, 487]]
##[[559, 499, 479, 536, 514, 526, 594, 616]]
##[[647, 501, 613, 609, 533, 657, 683]]
##[[666, 614, 636, 684, 660, 717]]
##[[686, 640, 766, 731, 782]]
##[[704, 801, 853, 792]]
##[[818, 900, 935]]
##[[995, 999]]
##[[1074]]
    
##19
##count = 0
##currentday = 2
##
##for year in range(1900, 2001):
##    if ((not year%4) and year%100) or not year%400:
##        days = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
##        daycount=366
##    else:
##        daycount=365
##        days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
##
##    for i in range(daycount):
##        currentday = currentday%7+1
##        if currentday == 1 and i in days and year>1900:
##            count += 1        
##print count

##20
##print sum(map(lambda x: int(x), list(str(math.factorial(100)))))

##21
def factors(n):
    s=set([])
    for i in range(1, int(n**0.5)+1):
        if not n%i:
            s.add(i)
            s.add(n/i)
    s.discard(n)
    return s
##
##s,t=0,set(range(0,10000))
##while t:
##    i = t.pop()
##    a = sum(factors(i))
##    if sum(factors(a)) == i and a!=i:
##        s += a+i
##        print a,i
##    t.discard(a)
##
##print s

##22 (file-dependant, done at home:D)

##23
##abundants = (filter(lambda x: sum(factors(x)) > x, range(28123)))
##x = set(range(28123))
##y = set(i+j for i in abundants for j in abundants)
##print sum(x - y)

##24
##import math
##c, l = 999999, []
##for i in range(9, 0, -1):
##    l += [int(c/math.factorial(i))]
##    c -= int(c/math.factorial(i))*math.factorial(i)
##    if c == 0:
##        break
##print l
## then manually

##25
##a = fib(10**1001)
##c=2
##while True:
##    t = a.next()
##    if t > 10**999:
##        print t
##        break
##    c+=1

##26
##import re
##from decimal import *
##getcontext().prec = 5000
##n=0
##for i in range(1,2500):
##    a = str(Decimal(1)/Decimal(i))[2:]
##    for j in range(600,1000):
##        if a[:j] == a[j: 2*j]:
##            
##            if j>n:
##                n=j
##                res = i
##            break
##print res

##27
##mx=0
##for a in range(-1000, 1001):
##
##    for b in range(-1000, 1001):
##
##        n=0
##        i=0
##        while isp(i**2+a*i+b):
##
##            n+=1
##            i+=1 
##        if n>mx:
##            m=a,b
##            mx = n
##print mx, m[0]*m[1]

##28
##s=1
##j=2
##init=1
##for i in range(1,501):
##    for i in range(4):
##        init+=j
##        s+=init
##
##    j+=2
##print s

##29
##s=set([])
##for i in range(2,101):
##    for j in range(2,101):
##        s.add(i**j)
##print len(s)

##30
##l=[]
##for i in range(2,1000000):
##    if i == sum(int(j)**5 for j in str(i)):
##        l+=[i]
##print sum(l)

##31
##def rec(togo, coins):
##    if not coins:
##        return 0
##    current, coins = coins[0], coins[1:]
##    c = 0
##    if not togo % current: 
##        c += 1
##    for i in range(0, togo, current):
##        c += rec(togo - i, coins)
##    return c
##
##print rec(200, [1,2,5,10,20,50,100,200])

##32
##results = set([])
##for i in range(1000, 9999):
##    opts = factors(i)
##    opts.discard(1)
##    for j in opts:
##        digits = set(i for i in str(i/j)+str(j)+str(i))
##        if '0' not in digits and len(digits) == 9:
##            results.add(i)
##            break
##print sum(results)

##33
##s = set([])
##for i in range(10,100):
##    for j in range(10,100):
##        if i!=j:
##            a1, a2, b1, b2 = str(i)[0], str(i)[1], str(j)[0], str(j)[1]
##            if a1 == b2 and b1 != '0':
##                if 1.0*i/j == 1.0*int(a2)/int(b1) and 1.0*i/j < 1:
##                    s.add(1.0*i/j)
##            if a2 == b1 and b2 != '0':
##                if 1.0*i/j == 1.0*int(a1)/int(b2) and 1.0*i/j < 1:
##                    s.add(1.0*i/j)
##                               
##print reduce(lambda x,y: x*y, s)  

##34
##for i in range(10, 1000000):
##    if sum(math.factorial(int(j)) for j in str(i)) == i:
##        print i

##35
##def rotate(string):
##    c = 0
##
##    while c != len(string):
##        c+=1
##        yield string[-c:]+string[:-c]
##c=0
##for i in range(2, 1000000):
##    t=True
##    a = rotate(str(i))
##    for j in a:
##        if not isp(int(j)):
##            t=False
##            break
##    if t:
##        c+=1

##36
##print sum(i for i in range(1,1000000) if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[2:][::-1])

##37
##c, n, s = 11, 0, []
##while n!=11:
##    c+=2
##    t=True
##    if not isp(c):
##        continue
##    for i in range(len(str(c))-1):
##
##        if not (isp(int(str(c)[:-i-1])) and isp(int(str(c)[i+1:]))):
##            t=False
##            break
##    if t:
##        n+=1
##        s+=[c]
##
##print sum(s)

##38
##def ispan(num, n):
##    pan = [str(i) for i in range(1,10)]
##    conc = ''.join(str(i*num) for i in range(1, n+1))
##    
##    if sorted(conc) == pan:
##        return conc
##    return False
##s=[]
##for i in range(10000):
##    for j in range(1,10):
##        a = ispan(i, j)
##        if a:
##            s+=[int(a)]
##print max(s)

##39
##d = {}
##for i in range(3, 1001):
##    d[i]=0
##for i in range(1,500):
##    for j in range(1,500):
##        k = (i**2+j**2)**0.5
##        if k-int(k) or i+j+k>1000:
##            continue
##        else:
##            d[int(i+j+k)]+=1
##
##mx = 0
##for i in d:
##    if d[i]>mx:
##        mx=d[i]
##        t=i
##print t


##40(ew)
##t=''.join(str(i) for i in range(1000000))
##print reduce(lambda x,y: int(x)*int(y), [t[1],t[10],t[100],t[1000],t[10000],t[100000],t[1000000]])

##41 (can't be 8 or 9 digits since 3 always divides such numbers)
##def thing(n, digits):
##    pan = [str(i) for i in range(1,digits+1)]
##    if sorted(str(n)) == pan:
##        return True
##    return False
##for i in itertools.permutations(range(7, 0, -1), 7):
##    num = int(''.join(str(j) for j in i))
##
##    if isp(num):
##        print num
##        break

##42 - at home, files are evil:(

##43
##divs=[2,3,5,7,11,13,17]
##s=0
##for i in itertools.permutations(range(9, -1, -1), 10):
##    num = ''.join(str(j) for j in i)
##
##    if num[0] == '0':
##        continue
##    t=True
##    for j in range(len(divs)):
##
##        if int(num[1+j:4+j]) % divs[j]:
##            t=False
##            break
##    if t:
##        s+=int(num)
##        print num
##print s

##44
##a = [int(1.0*n*(3*n-1)/2) for n in range(1,5000)]
##b = set(a)
##for i in range(1,2500):
##    for j in range(i+1,2500):
##        if abs(a[i]-a[j]) in b and a[i]+a[j] in b:
##            print i, j

##45
##pent = set([int(1.0*n*(3*n-1)/2) for n in range(1000,100000)])
##tri = set([int(1.0*n*(n+1)/2) for n in range(1000,100000)])
##hexa = set([int(1.0*n*(2*n-1)) for n in range(1000,100000)])
##print pent & tri & hexa

##46
##issquare = lambda x: False if x<=0 else not x**0.5 - int(x**0.5)
##primes = filter(isp, range(100000))
##opts = filter(lambda x: not isp(x), range(1, 10000, 2))
##for i in opts:
##    f=False
##    for j in primes:
##        if issquare((i-j)/2):
##            f=True
##            break
##    if not f:
##        print i

##47
##pfactors = lambda x: set(filter(isp, factors(x)))
##a=[pfactors(i) for i in range(500004)]
##for i in range(0, 500000):
##    if sum(len(a[j]) for j in range(i, i+4)) == 16:
##        print i
##        break

##48
##print sum(i**i % 10000000000 for i in range(1,1001))

##49
hsh = lambda x: sum(hash(i) for i in str(x))
##primes = [i for i in range(1000,10000) if isp(i)]
##d = {}
##for i in primes:
##    n1, n2 = i+3330, i+6660
##    if n1 in primes and n2 in primes:
##        if hsh(n1) == hsh(n2) == hsh(i):
##            print i, n1, n2

##50
##primes = filter(isp, range(10000))
##p2 = filter(isp, range(950000, 1000000))
##setprimes, setp2 = set(primes), set(p2)
##t = []
##for k in range(50):
##    mx, s, count = 0, 0, 0
##    for i in primes[k::]:
##        
##        s += i
##        count += 1
##        if s > 1000000:
##            t+= [(mx, rcount)]
##            break
##        if s in setprimes or s in setp2:
##            mx = s
##            rcount = count
##print reduce(lambda x, y: x if x[1]>y[1] else y,t)

##51
##whaaaaaat?
t = filter(isp, range(10000, 100000))




#52
##for i in range(1,1000000):
##    if hsh(i)==hsh(2*i)==hsh(3*i)==hsh(4*i)==hsh(5*i)==hsh(6*i):
##        print i
##        break

##53
##from math import *
##c=lambda n, r: factorial(n)/(factorial(r)*factorial(n-r))
##count=0
##for n in range(23,101):
##    if n%2:
##        for r in range(1, int((n/2))):
##            if c(n,r)>1000000:
##                count+=2
##        if c(n, n/2)>1000000:
##                count+=1
##            
##    else:
##        for r in range(1, int(n/2)+1):
##            if c(n,r)>1000000:
##                count+=2
##print count

##54

##58 euler
##def corners(n):
##    yield 1
##    c, d = 1, 2
##    for i in range(n):
##        for i in range(4):
##            c+=d
##            yield c
##        d+=2
##    
##t=[a for a in corners(14000)]
##b = map(lambda x: 1 if isp(x) else 0, t)
##res = 1
##c, l = 0, 0
##while res >= 0.1 or c<10:
##    if b[c]:
##        l+=1
##    c+=1
##    res = 1.0*l/c
##print c/2+1

