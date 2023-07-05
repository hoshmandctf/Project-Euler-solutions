# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_max_prime_coefficients():
    max_primes = 0
    max_product = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            while is_prime(n**2 + a*n + b):
                n += 1

            if n > max_primes:
                max_primes = n
                max_product = a * b

    return max_product


result = find_max_prime_coefficients()
print(result)
