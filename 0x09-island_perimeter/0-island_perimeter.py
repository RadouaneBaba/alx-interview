#!/usr/bin/python3
""" Island perimeter module """


def island_perimeter(grid):
    """return perimeter of island"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += (
                    4
                    - grid[i + 1][j]
                    - grid[i][j + 1]
                    - grid[i - 1][j]
                    - grid[i][j - 1]
                )
    return perimeter
