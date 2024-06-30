class RsaDecoder:
    def __init__(self, n, e):
        self._n = n
        self._e = e
        self._factors = []
        self._p = None
        self._q = None
        self._phi = None
        self._d = None

    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def factor(self, n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                pair = (i, n // i)
                if self.is_prime(i) and self.is_prime(n // i):
                    self._factors.append(pair)
                    return pair
        return None, None

    def set_p_q(self):
        p, q = self.factor(self._n)
        self._p = p
        self._q = q
        return self._p, self._q

    def get_p(self):
        if self._p is None:
            self.set_p_q()
        return self._p

    def get_q(self):
        if self._q is None:
            self.set_p_q()
        return self._q

    def set_phi(self):
        p = self.get_p()
        q = self.get_q()
        phi = (p - 1) * (q - 1)
        self._phi = phi
        return self._phi

    def get_phi(self):
        if self._phi is None:
            self.set_phi()
        return self._phi

    def egcd(self, a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = self.egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

    def mod_inverse(self, e, phi):
        g, x, y = self.egcd(e, phi)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % phi

    def set_d(self):
        phi = self.get_phi()
        self._d = self.mod_inverse(self._e, phi)
        return self._d

    def get_d(self):
        if self._d is None:
            self.set_d()
        return self._d

# try:
#     n = input('What is n: ')
#     n = int(n)
# except ValueError:
#     raise TypeError('n should be an integer')
#
# try:
#     e = input('What is e: ')
#     e = int(e)
# except ValueError:
#     raise TypeError('n should be an integer')
#
# rsa = RsaDecoder(n, e)
#
# print(rsa.get_phi())
# print(rsa.get_p())
# print(rsa.get_q())
# print(rsa.get_d())
