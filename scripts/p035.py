# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_rotations(num):
    num_str = str(num)
    rotations = []
    for i in range(len(num_str)):
        rotation = int(num_str[i:] + num_str[:i])
        rotations.append(rotation)
    return rotations

circular_prime_count = 0

for num in range(2, 1000000):
    if is_prime(num):
        is_circular_prime = True
        for rotation in get_rotations(num):
            if not is_prime(rotation):
                is_circular_prime = False
                break
        if is_circular_prime:
            circular_prime_count += 1

print("Number of circular primes below one million:", circular_prime_count)
