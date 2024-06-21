#!/usr/bin/python3
""" Prime Game Implementation """


def generate_primes(n):
    """doc doc"""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def play_round(n):
    """doc doc"""
    primes = generate_primes(n)
    turn = 0
    while primes:
        prime = primes[0]
        primes = [p for p in primes if p % prime != 0]
        turn = 1 - turn
    return "Ben" if turn == 0 else "Maria"


def isWinner(x, nums):
    """doc doc"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
