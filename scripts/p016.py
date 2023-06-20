# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def sum_of_digits(number):
    # Convert the number to a string
    number_str = str(number)

    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in number_str)

    return digit_sum

# Calculate 2^1000
power_of_2 = 2 ** 1000

# Calculate the sum of the digits
digit_sum = sum_of_digits(power_of_2)

print("The sum of the digits of 2^1000 is:", digit_sum)
