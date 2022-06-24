import random
import math

class KeyPair:

    def __init__(self):
        self._privateKey = privateKey
        self.publickey = publicKey

    #def RSA_method(self):
        #self._privateKey = random.getrandbits(512)       #цей клас ще не реалізований до кінця!!!!!
        #self.publicKey = random.getrandbits(512)
        #n = self._privateKey * self.publicKey


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
        if n:
            return ret * n
        else:
            return ret










