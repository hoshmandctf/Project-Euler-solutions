# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

import math

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(digits)
permutation_index = 1000000

# Calculate factorial of n
factorial = math.factorial(n)

# Ensure permutation index is within range
if permutation_index > factorial:
    print("Permutation index is out of range.")
    exit()

permutation_index -= 1

# Initialize variables
result = []
available_digits = digits[:]

# Generate lexicographic permutation
for i in range(n, 0, -1):
    index = permutation_index // math.factorial(i-1)
    
    digit = available_digits[index]
    
    result.append(digit)
    
    available_digits.remove(digit)
    
    permutation_index %= math.factorial(i-1)

# Convert the result list to a string
result_str = ''.join(str(digit) for digit in result)

# Print the millionth lexicographic permutation
print(result_str)
