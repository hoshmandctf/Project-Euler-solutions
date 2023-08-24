# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def is_palindromic(n):
    return str(n) == str(n)[::-1]

def solve_project_euler_problem(limit):
    total_sum = 0
    for num in range(limit):
        if is_palindromic(num) and is_palindromic(bin(num)[2:]):
            total_sum += num
    return total_sum

limit = 1000000
result = solve_project_euler_problem(limit)
print("The sum of all numbers palindromic in both base 10 and base 2, less than one million, is:", result)
