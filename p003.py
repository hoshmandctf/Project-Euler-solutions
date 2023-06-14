# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def largest_prime_factor(number):
    i = 2  # Starting prime factor
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    return number

# Define the number and call the function
number = 600851475143
result = largest_prime_factor(number)

print("The largest prime factor of", number, "is:", result)
