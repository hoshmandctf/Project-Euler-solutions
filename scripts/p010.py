# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def sieve_of_eratosthenes(n):
    # Create a boolean array "is_prime[0..n]" and initialize all entries it as true.
    # A value in is_prime[i] will finally be false if i is Not a prime, else true.
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n+1, p):
                is_prime[i] = False
        p += 1

    return [i for i in range(n+1) if is_prime[i]]


limit = 2000000
primes = sieve_of_eratosthenes(limit - 1)
prime_sum = sum(primes)

print("The sum of all primes below two million:", prime_sum)
