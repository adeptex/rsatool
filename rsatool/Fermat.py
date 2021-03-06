from libnum import *
import gmpy

class Fermat():
    def __init__(self, n, e, limit=10000):
        self.n = n
        self.e = e
        self.d = None
        self.p = None
        self.q = None
        self.limit = limit

    def crack(self):
        a = gmpy.sqrt(self.n)
        max = a + self.limit
        while a < max:
            b2 = a*a - self.n
            if b2 >= 0:
                b = gmpy.sqrt(b2)
                if b*b == b2:
                    break
            a += 1
        if a < max:
            self.p = long(a+b)
            self.q = long(a-b)
            phi = (self.p - 1) * (self.q - 1)
            if has_invmod(self.e, phi):
                self.d = long(invmod(self.e, phi))
                return True
        else:
            return False
