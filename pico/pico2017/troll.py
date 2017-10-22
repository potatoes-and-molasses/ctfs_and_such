import socket
import re
import urllib
import gmpy2
gmpy2.get_context().precision = 4096
q = urllib.urlopen('https://webshell2017.picoctf.com/static/e73fa3dfd7075e29783f4c8ac68b7f62/clue.txt').read()
t = q.split('\n')[:-1]
for i in t:
	r = i.replace(':','=')
	exec r

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
def int2Text(number, size):
    """Convert an integer into a text string"""
    text = "".join([chr((number >> j) & 0xff)
                    for j in reversed(range(0, size << 3, 8))])
    return text.lstrip("\x00")
#crt
tb = c1*(n2*n3)*modinv(n2*n3,n1)
tc = c2*(n1*n3)*modinv(n1*n3,n2)
td = c3*(n1*n2)*modinv(n1*n2,n3)
c = (tb+tc+td) % (n1*n2*n3)


root = int(gmpy2.root(c,3))
print hex(root)[2:-1].decode('hex')
