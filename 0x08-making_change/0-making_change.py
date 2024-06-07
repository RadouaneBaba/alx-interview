#!/usr/bin/python3
"""making change implementation"""


def min_skip(a, b):
    if a == -1 and b == -1:
        return -1
    if a == -1 and b > -1:
        return b + 1
    if a > -1 and b == -1:
        return a
    return min(a, b + 1)


def makeChange(coins, total, cache=None):
    """make change implementation"""
    if total <= 0:
        return 0

    if cache is None:
        cache = {}

    if total in cache:
        return cache[total]
    solution = -1
    for coin in coins:
        new_total = total - coin
        if new_total < 0:
            continue
        solution = min_skip(solution, makeChange(coins, new_total, cache))
    cache[total] = solution
    return solution
