# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def factorial_digit_sum(n):
    # Calculate the factorial of n
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i

    # Sum up the digits in the factorial
    digit_sum = 0
    while factorial > 0:
        digit_sum += factorial % 10
        factorial //= 10

    return digit_sum

# Calculate the sum of the digits in 100!
digit_sum = factorial_digit_sum(100)
print("The sum of the digits in 100! is:", digit_sum)
