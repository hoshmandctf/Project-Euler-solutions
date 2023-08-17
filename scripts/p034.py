# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_curious_number(n):
    digit_factorials_sum = sum(factorial(int(digit)) for digit in str(n))
    return n == digit_factorials_sum

curious_numbers = []

# We can set an upper bound for the search space.
# Since the maximum digit factorial sum for a 7-digit number is 9! * 7 = 2540160,
# it's reasonable to set the upper bound to be below this value.
for num in range(10, 2540160):
    if is_curious_number(num):
        curious_numbers.append(num)

sum_of_curious_numbers = sum(curious_numbers)
print("Sum of all numbers equal to the sum of factorial of their digits:", sum_of_curious_numbers)
