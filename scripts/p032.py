# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def is_pandigital(s):
    return len(s) == 9 and set(s) == set("123456789")

pandigital_products = set()

# The maximum value for the multiplicand and multiplier can be derived from the following equation:
# max(multiplicand) + max(multiplier) = max(product)
# Since 2-digit * 3-digit = 4-digit and 1-digit * 4-digit = 4-digit, the maximum possible values are:
# max(multiplicand) = 99, max(multiplier) = 9999, max(product) = 9999
for multiplicand in range(1, 100):
    for multiplier in range(1, 10000):
        product = multiplicand * multiplier
        identity_str = str(multiplicand) + str(multiplier) + str(product)
        if len(identity_str) > 9:
            break
        if len(identity_str) == 9 and is_pandigital(identity_str):
            pandigital_products.add(product)

sum_of_pandigital_products = sum(pandigital_products)
print("Sum of all products with pandigital identity:", sum_of_pandigital_products)
