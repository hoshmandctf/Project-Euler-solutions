# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def is_pentagonal(num):
    n = (1 + (1 + 24 * num) ** 0.5) / 6
    return n.is_integer()

def is_hexagonal(num):
    n = (1 + (1 + 8 * num) ** 0.5) / 4
    return n.is_integer()

def find_next_triangle():
    n = 286  # Starting from the next value after 285
    while True:
        triangle = n * (n + 1) // 2
        if is_pentagonal(triangle) and is_hexagonal(triangle):
            return triangle
        n += 1

result = find_next_triangle()
print("The next triangle number that is also pentagonal and hexagonal is:", result)
