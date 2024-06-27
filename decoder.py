class RSA:
    class RSA:
        def __init__(self, n, e):
            self._factors = []  # Initialize as an empty list
            self._n = n
            self._e = e
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

        def get_p(self):
            p, q = self.factor(self._n)
            return int(p) if p else None

        def get_q(self):
            p, q = self.factor(self._n)
            return int(q) if q else None

        def phi(self):
            p = self.get_p()
            q = self.get_q()
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

rsa = RSA(n,e)