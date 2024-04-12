#!/usr/bin/python3

""" technical interview prep pascal """


def pascal_triangle(n):
    """ returns a listof lists of integers representing the Pascal triangle"""
    if n <= 0:
        return []
    pascal = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(pascal[i - 1][j] + pascal[i - 1][j - 1])
        pascal.append(row)

    return pascal
