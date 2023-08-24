# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i+1])):
            return False
    return True

def find_truncatable_primes(count):
    truncatable_primes = []
    num = 11  # Starting from 11, as 2, 3, 5, and 7 are not considered truncatable primes
    while len(truncatable_primes) < count:
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
        num += 2  # Increment by 2 to skip even numbers
    return truncatable_primes

count = 11  # Number of truncatable primes to find
truncatable_primes = find_truncatable_primes(count)
sum_of_truncatable_primes = sum(truncatable_primes)

print("The sum of the only eleven truncatable primes is:", sum_of_truncatable_primes)
