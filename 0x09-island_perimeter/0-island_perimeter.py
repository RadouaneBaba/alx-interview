#!/usr/bin/python3
""" Island perimeter module """


def island_perimeter(grid):
    """return perimeter of island"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i != 0:
                    perimeter -= grid[i - 1][j]
                if j != 0:
                    perimeter -= grid[i][j - 1]
                if i != len(grid) - 1:
                    perimeter -= grid[i + 1][j]
                if j != len(grid[i]) - 1:
                    perimeter -= grid[i][j + 1]
    return perimeter
