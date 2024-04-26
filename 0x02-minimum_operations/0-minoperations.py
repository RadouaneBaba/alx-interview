#!/usr/bin/python3
""" Minimum Operations implementation """


def minOperations(n):
    """ Minimum number of operations """
    prime_factors = [2, 3, 5, 7, 11, 13, 17, 19]
    if n <= 0:
        return 0
    idx = 0
    steps = 0
    while (n != 1):
        while (n % prime_factors[idx] != 0):
            idx += 1
        n /= prime_factors[idx]
        steps += prime_factors[idx]

    return steps
