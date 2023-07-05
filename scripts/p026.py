# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def find_longest_recurring_cycle(limit):
    longest_cycle = 0
    number = 0

    for d in range(2, limit):
        remainder = 1
        remainders = {}

        while remainder != 0 and remainder not in remainders:
            remainders[remainder] = len(remainders)
            remainder = (remainder * 10) % d

        if remainder != 0:
            cycle_length = len(remainders) - remainders[remainder]
            if cycle_length > longest_cycle:
                longest_cycle = cycle_length
                number = d

    return number

limit = 1000
result = find_longest_recurring_cycle(limit)
print(result)
