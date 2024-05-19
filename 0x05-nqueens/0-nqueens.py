#!/usr/bin/python3
"""N-queens Implementation"""
import sys


def check_int(n):
    """check if n is int"""
    try:
        int(n)
        return True
    except ValueError:
        return False


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not check_int(sys.argv[1]):
    print("N must be a number")
    sys.exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)


def n_queens(n, path=None):
    """N-queens function to handle recursive calls"""
    if path and len(path) == n:
        print(path)
        return path
    row = 0
    if path:
        row = path[-1][0] + 1

    for col in range(n):
        if not path:
            n_queens(n, [[row, col]])
        else:
            valid = True
            for choice in path:
                diag = row - choice[0]
                if col in [choice[1], choice[1] - diag, choice[1] + diag]:
                    valid = False
            if valid:
                n_queens(n, path + [[row, col]])


n_queens(int(sys.argv[1]))
