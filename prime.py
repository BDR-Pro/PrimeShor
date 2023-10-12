from logging import raiseExceptions
import math
class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message


def factorize(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        q, r = divmod(n, i)
        if r == 0:
            return i,q 
    raise MyCustomException("Can not find factors")



def isPrime(n):
    for i in range(2, int(math.isqrt(n)) + 1):
        q, r = divmod(n, i)
        if r == 0:
            return False  # Found a factor, not prime
    return True  # No factors found, prime
