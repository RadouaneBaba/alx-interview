#!/usr/bin/python3
""" Minimum Operations implementation """


def minOperations(n):
    """ Minimum number of operations """
    if n <= 0:
        return 0
    factor = 2
    steps = 0
    while (n != 1):
        while (n % factor != 0):
            factor += 1
        n /= factor
        steps += factor

    return steps
