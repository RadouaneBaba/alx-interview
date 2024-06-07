#!/usr/bin/python3
"""making change implementation"""


def makeChange(coins, total, cache=None):
    """
    makechange implementation
    """
    if cache is None:
        cache = {}

    if total <= 0:
        return 0

    if total in cache:
        return cache[total]

    min_coins = float("inf")
    for coin in coins:
        if coin <= total:
            sub_result = makeChange(coins, total - coin, cache)
            if sub_result != -1:
                min_coins = min(min_coins, sub_result + 1)

    cache[total] = -1 if min_coins == float("inf") else min_coins
    return cache[total]
