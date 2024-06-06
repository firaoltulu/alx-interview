#!/usr/bin/python3
"""this fuction Change making module.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    loc_min_coins = [float("inf")] * (total + 1)
    loc_min_coins[0] = 0

    for loc_coin in coins:
        for i in range(loc_coin, total + 1):
            loc_min_coins[i] = min(loc_min_coins[i], loc_min_coins[i - loc_coin] + 1)

    return loc_min_coins[total] if loc_min_coins[total] != float("inf") else -1
