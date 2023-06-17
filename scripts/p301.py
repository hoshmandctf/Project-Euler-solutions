# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

# note that solving this problem by brute force may take a significant amount of time due to the large range of values.
count = 0
for n in range(1, 2**30 + 1):
    nim_sum = n ^ (2*n) ^ (3*n)
    if nim_sum == 0:
        count += 1

print("The number of positive integers satisfying X(n, 2n, 3n) = 0 is:", count)
