class RsaDecoder:
    def __init__(self, n, e):
        self._n = n
        self._e = e
        self._factors = []
        self._p = None
        self._q = None
        self._phi = None

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


