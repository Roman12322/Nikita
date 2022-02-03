from math import sqrt, ceil, pow
import unittest

class SieveOfAtkin:
    def __init__(self, limit):
        self.limit = limit
        self.primes = []
        self.sieve = [False] * (self.limit + 1)

    def flip(self, prime):
        try:
            self.sieve[prime] = True if self.sieve[prime] == False else False
        except KeyError:
            pass

    def invalidate(self, prime):
        try:
            if self.sieve[prime] == True: self.sieve[prime] = False
        except KeyError:
            pass

    def isPrime(self, prime):
        try:
            return self.sieve[prime]
        except KeyError:
            return False

    def getPrimes(self):
        testingLimit = int(ceil(sqrt(self.limit)))

        for i in range(testingLimit):
            for j in range(testingLimit):
                # n = 4*i^2 + j^2
                n = 4 * int(pow(i, 2)) + int(pow(j, 2))
                if n <= self.limit and (n % 12 == 1 or n % 12 == 5):
                    self.flip(n)

                # n = 3*i^2 + j^2
                n = 3 * int(pow(i, 2)) + int(pow(j, 2))
                if n <= self.limit and n % 12 == 7:
                    self.flip(n)

                # n = 3*i^2 - j^2
                n = 3 * int(pow(i, 2)) - int(pow(j, 2))
                if n <= self.limit and i > j and n % 12 == 11:
                    self.flip(n)

        for i in range(5, testingLimit):
            if self.isPrime(i):
                k = int(pow(i, 2))
                for j in range(k, self.limit, k):
                    self.invalidate(j)

        self.primes = [2, 3] + [x for x in range(len(self.sieve)) if self.isPrime(x) and x >= 5]
        return self.primes

def Primes(value):
    sieve = SieveOfAtkin(400)
    buffer = sieve.getPrimes()
    res = []
    for i in range(value):
        res.append(buffer[i])
    return res

class primes_testing(unittest.TestCase):
    def setUp(self):
        pass

    def test_primes_testing1(self):
        result = Primes(0)
        self.assertEqual([], result)

    def test_primes_testing2(self):
        result = Primes(3)
        self.assertEqual([2, 3, 5], result)

    def test_primes_testing3(self):
        result = Primes(5)
        self.assertEqual([2, 3, 5, 7, 11], result)

    def test_primes_testing4(self):
        test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
                137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197]
        result = Primes(45)
        self.assertEqual(test, result)
