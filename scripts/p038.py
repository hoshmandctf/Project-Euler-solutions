# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def is_pandigital(number):
    return ''.join(sorted(str(number))) == '123456789'

def generate_concatenated_product(number, n):
    concatenated_product = ''
    for i in range(1, n+1):
        concatenated_product += str(number * i)
    return int(concatenated_product)

def find_largest_pandigital_concatenated_product():
    largest_pandigital = 0
    for num in range(1, 10000):  # Upper bound chosen based on observation
        n = 1
        concatenated_product = generate_concatenated_product(num, n)
        while len(str(concatenated_product)) <= 9:
            if is_pandigital(concatenated_product):
                largest_pandigital = max(largest_pandigital, concatenated_product)
            n += 1
            concatenated_product = generate_concatenated_product(num, n)
    return largest_pandigital

largest_pandigital = find_largest_pandigital_concatenated_product()
print("The largest 1 to 9 pandigital 9-digit number is:", largest_pandigital)
