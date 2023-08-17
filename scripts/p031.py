# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def count_coin_combinations(target, coins):
    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]

    return ways[target]

target_amount = 200  # £2 in pence
coin_values = [1, 2, 5, 10, 20, 50, 100, 200]

result = count_coin_combinations(target_amount, coin_values)
print("Number of different ways to make £2:", result)
