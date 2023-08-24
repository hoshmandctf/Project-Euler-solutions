# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

from collections import Counter

def find_maximized_perimeter():
    max_solutions = 0
    max_perimeter = 0

    for perimeter in range(3, 1001):
        solutions = Counter()

        for a in range(1, perimeter // 2):
            for b in range(a, perimeter // 2):
                c = perimeter - a - b
                if a * a + b * b == c * c:
                    solutions[a + b + c] += 1

        num_solutions = max(solutions.values(), default=0)
        if num_solutions > max_solutions:
            max_solutions = num_solutions
            max_perimeter = perimeter

    return max_perimeter

maximized_perimeter = find_maximized_perimeter()
print("The value of p ≤ 1000 for which the number of solutions is maximized is:", maximized_perimeter)
