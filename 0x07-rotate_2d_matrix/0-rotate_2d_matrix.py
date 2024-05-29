#!/usr/bin/python3
"""rotate 2d matrix module"""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix"""
    n = len(matrix)
    for i in range(int(n / 2)):
        for j in range(i, n - i - 1):
            a = n - 1
            temp1 = matrix[j][a - i]
            matrix[j][a - i] = matrix[i][j]

            temp2 = matrix[a - i][a - j]
            matrix[a - i][a - j] = temp1

            temp1 = matrix[a - j][i]
            matrix[a - j][i] = temp2

            matrix[i][j] = temp1
