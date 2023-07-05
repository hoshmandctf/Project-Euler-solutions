# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf


def sum_of_digit_fifth_powers():
    result = 0

    for number in range(10, 354294):  # Upper limit determined by examining the number of digits
        digit_sum = 0
        n = number

        while n > 0:
            digit = n % 10
            digit_sum += digit ** 5
            n //= 10

        if digit_sum == number:
            result += number

    return result


result = sum_of_digit_fifth_powers()
print(result)
