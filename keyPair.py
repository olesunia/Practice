import random
import math

class KeyPair:

    def RSA_method(self):
        self.p = random.getrandbits(512)     #спробувала згенерувати пару ключів методом RSA, проте
        self.q = random.getrandbits(512)      # не впевнена, що зробила це правльно, так як
        n = self.p * self.q                    # не розумію до кінця ООП
        self.n = n
        self.ret = self.euler_func(self.n)
        e = random.randrange(2, self.ret - 1)
        self.e = e
        while math.gcd(self.e, self.ret) != 1:
            self.e = random.randrange(2, self.ret - 1)

        self.e = e
        d = self.euclid(self.p, self.q)
        self.d = d
        while (self.d * self.e) % self.ret != 1:
            self.d = self.euclid(self.p, self.q)
        self.d = d

        return self.n, self.e, self.d

    def euler_func(self,n):
        ret = 1
        for i in range(2,math.floor((self.n)**0.5)):
            p = 1
            while not self.n % i:
                p *= i
                self.n /= i
            p /= i
            if p >= 1:
                ret = ret * p * (i - 1)
        self.n -= 1
        if self.n:
            return ret * self.n
        else:
            return ret

    def euklid(self, a, b) :
        if b == 0:
            return a
        d = self.euklid(b, a % b)
        self.d = d
        return self.d

    def genKeyPair(self,n,e,d):
        privateKey = [self.n,self.d]
        self._privateKey = privateKey
        publicKey = [self.n,self.e]
        self.publickey = publicKey

        return self._privateKey, self.publicKey

    def printKeyPair(self,privateKey,publicKey):

        print("KeyPair are: ",self.privateKey, self.publicKey)


KeyPair()









