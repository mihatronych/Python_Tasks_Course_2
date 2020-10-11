import itertools
import math

def primes():
    num = 1
    while True:
        num += 1
        if (math.factorial(num - 1) + 1) % num == 0:
            yield num



print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
