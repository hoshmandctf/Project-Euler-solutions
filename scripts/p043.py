# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

from itertools import permutations

def is_special_pandigital(number):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        sub_num = int(number[i:i+3])
        if sub_num % primes[i - 1] != 0:
            return False
    return True

def find_special_pandigital_sum():
    pandigital_digits = '0123456789'
    special_pandigital_sum = 0

    for perm in permutations(pandigital_digits):
        number = ''.join(perm)
        if is_special_pandigital(number):
            special_pandigital_sum += int(number)

    return special_pandigital_sum

result = find_special_pandigital_sum()
print("The sum of all 0 to 9 pandigital numbers with the specified property is:", result)
