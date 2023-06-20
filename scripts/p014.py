# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def collatz_sequence_length(n, cache):
    if n in cache:
        return cache[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        length = 1 + collatz_sequence_length(n // 2, cache)
    else:
        length = 1 + collatz_sequence_length(3 * n + 1, cache)
    cache[n] = length
    return length

def find_longest_collatz_chain(limit):
    max_length = 0
    max_starting_number = 0
    cache = {}

    for n in range(1, limit):
        length = collatz_sequence_length(n, cache)
        if length > max_length:
            max_length = length
            max_starting_number = n

    return max_starting_number

# Call the function to find the starting number that produces the longest chain
result = find_longest_collatz_chain(1000000)
print("The starting number under one million that produces the longest chain is:", result)
