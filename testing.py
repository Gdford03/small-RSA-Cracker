def is_prime(num):
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
def factor(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            pair = (i, n // i)
            if is_prime(i) and is_prime(n // i):
                return pair
    return None, None


def get_p(n):
    p, q = factor(n)
    return int(p)
def get_q(n):
    p, q = factor(n)
    return int(q)



def phi( p, q):
    phi = (p - 1) * (q - 1)
    return phi

print(factor(72217))
print(get_p(72217))
print(get_q(72217))