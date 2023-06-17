# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def get_triangle_number(n):
    return (n * (n + 1)) // 2

def get_num_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2
    if int(n**0.5)**2 == n:
        count -= 1
    return count

target_divisors = 500
n = 1
while True:
    triangle_number = get_triangle_number(n)
    divisors = get_num_divisors(triangle_number)
    if divisors > target_divisors:
        break
    n += 1

print("The first triangle number with over five hundred divisors is:", triangle_number)
