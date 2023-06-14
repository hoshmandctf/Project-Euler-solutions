# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def sum_even_fibonacci(limit):
    sum = 0
    fib_1 = 1  # First Fibonacci number
    fib_2 = 2  # Second Fibonacci number

    # Iterate until the current Fibonacci number exceeds the limit
    while fib_1 <= limit:
        if fib_1 % 2 == 0:
            sum += fib_1

        # Generate the next Fibonacci number
        fib_1, fib_2 = fib_2, fib_1 + fib_2

    return sum

# Call the function and print the result
result = sum_even_fibonacci(4000000)
print("The sum of even-valued terms in the Fibonacci sequence not exceeding 4 million is:", result)
