# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def find_pythagorean_triplet(sum):
    for a in range(1, sum):
        for b in range(a + 1, sum):
            c = sum - a - b
            if a**2 + b**2 == c**2:
                return a, b, c

# Find the Pythagorean triplet
target_sum = 1000
a, b, c = find_pythagorean_triplet(target_sum)

# Calculate the product
product = a * b * c

# Print the result
print("The product of the Pythagorean triplet is:", product)
