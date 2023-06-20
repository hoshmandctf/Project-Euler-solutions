# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

"""
this code may take some time to execute since it involves generating abundant numbers and checking their sums.
"""
def get_proper_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def is_abundant(n):
    divisors = get_proper_divisors(n)
    return sum(divisors) > n

def get_abundant_numbers(limit):
    abundant_numbers = []
    for i in range(1, limit + 1):
        if is_abundant(i):
            abundant_numbers.append(i)
    return abundant_numbers

def can_be_expressed_as_sum(n, abundant_numbers):
    for i in abundant_numbers:
        if i > n // 2:
            break
        if n - i in abundant_numbers:
            return True
    return False

def get_numbers_cannot_be_sum_of_abundant(limit):
    abundant_numbers = get_abundant_numbers(limit)
    numbers_cannot_be_sum = []
    for i in range(1, limit + 1):
        if not can_be_expressed_as_sum(i, abundant_numbers):
            numbers_cannot_be_sum.append(i)
    return numbers_cannot_be_sum

limit = 28123
numbers_cannot_be_sum = get_numbers_cannot_be_sum_of_abundant(limit)
sum_numbers_cannot_be_sum = sum(numbers_cannot_be_sum)
print("The sum of all the positive integers which cannot be written as the sum of two abundant numbers is:", sum_numbers_cannot_be_sum)
