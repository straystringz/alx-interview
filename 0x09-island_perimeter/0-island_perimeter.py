#!/usr/bin/python3
"""returns_ the perimeter of the island described in grid"""


def island_perimeter(grid):
    """returns_ the perimeter of the island described in grid"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                # cells with 2 sides touching other cells on top and bottm
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                # cells with 2 sides touching other cells <- and ->
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
