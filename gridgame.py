# This file is used to generate the grid game
import random


def generateGrid(len: int, n: int):
    """
    Generates a new grid with n squares coloured in
    """

    # Create an n x n grid
    arr = [[0] * len for i in range(len)]

    # Create a hashset to keep track of generated tuples.
    h_set = set()
    current_count_colour = 0

    while current_count_colour < n:
        x = random.randint(0, len - 1)
        y = random.randint(0, len - 1)
        if (x, y) in h_set:
            continue
        h_set.add((x, y))
        arr[x][y] = 1
        current_count_colour += 1
    return arr


def compareGrid(orig_arr, new_arr):
    """
    Compares grids and returns the amount of different squares
    i.e.
    """
    height = len(orig_arr)
    width = len(orig_arr[0])
    score = height * width

    for row in range(height):
        for col in range(width):
            if new_arr[row][col] != orig_arr[row][col]:
                score -= 1

    return score / (height * width)
