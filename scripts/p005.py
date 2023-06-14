# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def smallest_divisible(start, end):
    current_lcm = start
    for i in range(start + 1, end + 1):
        current_lcm = lcm(current_lcm, i)
    return current_lcm

smallest_number = smallest_divisible(1, 20)
print(smallest_number)
