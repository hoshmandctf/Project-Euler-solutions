# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def is_palindrome(number):
    # Convert the number to a string and check if it reads the same forwards and backwards
    return str(number) == str(number)[::-1]

def find_largest_palindrome():
    largest_palindrome = 0

    # Iterate through all possible combinations of two 3-digit numbers
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product < largest_palindrome:
                # If the product is smaller than the largest palindrome found so far, break the loop
                break
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome

# Call the function to find the largest palindrome
result = find_largest_palindrome()
print("The largest palindrome made from the product of two 3-digit numbers is:", result)
