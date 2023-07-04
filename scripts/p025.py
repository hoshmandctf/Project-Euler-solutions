# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def fibonacci_digits(digits):
    # Initialize Fibonacci sequence with first two terms
    fib_sequence = [1, 1]
    index = 2

    # Generate Fibonacci sequence until a term with desired number of digits is found
    while len(str(fib_sequence[-1])) < digits:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        index += 1

    return index

# Calculate the index of the first term with 1000 digits
index = fibonacci_digits(1000)

# Print the result
print(index)
