# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def divisor_sum(n):
    # Calculate the sum of proper divisors of n
    div_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            div_sum += i
            if i != n // i:
                div_sum += n // i
    return div_sum

def sum_of_amicable_numbers(limit):
    amicable_sum = 0
    for n in range(2, limit):
        div_sum = divisor_sum(n)
        if div_sum != n and divisor_sum(div_sum) == n:
            amicable_sum += n
    return amicable_sum

# Calculate the sum of all amicable numbers under 10000
amicable_sum = sum_of_amicable_numbers(10000)
print("The sum of all amicable numbers under 10000 is:", amicable_sum)
