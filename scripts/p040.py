# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def champernowne_digit(n):
    champernowne = "".join(str(i) for i in range(1, n + 1))
    return int(champernowne[n - 1])

positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
result = 1

for pos in positions:
    result *= champernowne_digit(pos)

print("The value of the expression is:", result)
