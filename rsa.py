Extended gcd
def exgcd(a,b): # asumsi b>a
    if (b<a) :
        (a,b) = (b,a)
        
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a!= 0:
        q, b, a = b//a, a, b%a
        y0, y1 = y1, y0 - q*y1
        x0, x1 = x1, x0 - q*x1
        
    return (b, x0, y0)

from random import randrange

class RSA :    # RSA sbg kelas (obyek oriented)

    def __init__(self, p, q) : # konstruktor
        self.p=p
        self.q=q
        # key generation: hitung phi,e,d
        phi = (p-1)*(q-1)
        # cari e*d + phi*Y = 1 via exgcd
        d=-1
        while d<0 :
            e = randrange(2, phi)
            (x,d,Y) = exgcd(e, phi)
            if x> 1 :
                d = -1
                
        # init variabel
        self.n=p*q
        self.e=e
        self.d=d
        self.p=p
        self.q=q

    def getKp(self) : # kunci publik
        return (self.e, self.n)

    def getKs(self) : # kunci secret
        return (self.d, self.p, self.q)

    def encrypt(self,m) : # return cipher c
        return

    def decrypt(self,c) : # return plaintext m
        return
        
  c= RSA (11,33)
  print c.getkp()
  print c.getks()
  c= RSA (11,31)
  print c.getkp()
  print c.getks()