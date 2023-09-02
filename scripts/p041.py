# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

import itertools
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def largest_pandigital_prime():
    largest_pandigital = 0
    digits = "123456789"

    # We'll start with n = 9 and go down to n = 1, looking for the largest pandigital prime
    for n in range(9, 0, -1):
        pandigital_permutations = itertools.permutations(digits[:n], n)
        pandigital_numbers = [int("".join(perm)) for perm in pandigital_permutations]
        pandigital_numbers.sort(reverse=True)

        for num in pandigital_numbers:
            if is_prime(num):
                largest_pandigital = num
                break
        
        if largest_pandigital != 0:
            break

    return largest_pandigital

result = largest_pandigital_prime()
print("The largest n-digit pandigital prime is:", result)
