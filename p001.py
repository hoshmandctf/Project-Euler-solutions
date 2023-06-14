# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def sum_of_multiples(limit):
    sum = 0
    for num in range(limit):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum

# Call the function and print the result
result = sum_of_multiples(1000)
print("The sum of all multiples of 3 or 5 below 1000 is:", result)
