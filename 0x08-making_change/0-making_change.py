#!/usr/bin/python3
"""making change implementation"""


def makeChange(coins, total):
    """
    make change implementation
    """
    # Handle base cases
    if total <= 0:
        return 0
    if not coins:
        return -1
    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float("inf") else -1
