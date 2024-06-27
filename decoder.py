class RsaDecoder:
    def __init__(self, n, e):
        self._n = n
        self._e = e
        self._factors = []
        self._p = int()
        self._q = int()
        self._phi = int()

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

    def set_p(self):
        p, q = self.factor(self._n)
        self._p = p
        return self._p

    def set_q(self):
        p, q = self.factor(self._n)
        self._q = q
        return self._q

    def phi(self):
        p = self._p
        q = self._q
        phi = (p - 1) * (q - 1)
        self._phi = phi
        return self._phi


try:
    n = input('What is n: ')
    n = int(n)
except ValueError:
    raise TypeError('n should be an integer')

try:
    e = input('What is e: ')
    e = int(e)
except ValueError:
    raise TypeError('n should be an integer')

rsa = RsaDecoder(n, e)
