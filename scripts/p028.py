# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def sum_diagonal_numbers(side_length):
    if side_length == 1:
        return 1

    diagonal_sum = 1
    current_number = 1
    step = 2

    while step <= side_length:
        for _ in range(4):
            current_number += step
            diagonal_sum += current_number

        step += 2

    return diagonal_sum

side_length = 1001
result = sum_diagonal_numbers(side_length)
print(result)
