# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def generate_pentagonal_numbers(limit):
    pentagonals = set()
    for n in range(1, limit + 1):
        pentagonal = n * (3 * n - 1) // 2
        pentagonals.add(pentagonal)
    return pentagonals

def find_minimized_pentagonal_difference():
    limit = 3000
    pentagonals = generate_pentagonal_numbers(limit)
    min_difference = float('inf')

    for pj in pentagonals:
        for pk in pentagonals:
            if pj != pk:
                if pj + pk in pentagonals and abs(pk - pj) in pentagonals:
                    difference = abs(pk - pj)
                    if difference < min_difference:
                        min_difference = difference

    return min_difference

result = find_minimized_pentagonal_difference()
print("The value of D for the pair of pentagonal numbers is:", result)
