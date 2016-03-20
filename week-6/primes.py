#!/usr/bin/env python



def genPrimes():
    
    def isPrime(num):
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True

    x = 2
    while True:
        if isPrime(x):
            yield x
            x += 1

