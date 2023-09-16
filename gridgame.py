#This file is used to generate the grid game
import random


def generateGrid(len: int, n: int):
    """
    Generates a new grid with n squares coloured in
    """

    #Create an n x n grid
    arr = [[0]*len]*len

    #Create a hashset to keep track of generated tuples.
    h_set = set()
    current_count_colour = 0

    while(current_count_colour < n):
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        if((x,y) in set):
            continue
        arr[x][y] = 1
        current_count_colour+=1

    return arr

def compareGrid(orig_arr, new_arr):

    """
    Compares grids and returns an accuracy measure..
    i.e. 
    """

    wrong_count = 0
    len = len(orig_arr[0])
    for i in range(len):
        for j in range(len):
            if(new_arr[i][j] != orig_arr[i][j]):
                wrong_count+=1
    return wrong_count
            
            







