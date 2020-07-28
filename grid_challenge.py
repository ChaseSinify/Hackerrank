#!/bin/python3

import math
import os
import random
import re
import sys


#problem is literally broken as one test case DOES NOT give a SQUARE
#would be easy to fix by either party

"""
n = len grid
grid = square matrix of lowercase ascii chars
"""
def gridChallenge(n, grid):
    #sorting rows first
    for i in range(n):
        grid[i] = sorted(grid[i])
    
    #checking columns NOTE: grid is square
    for i in range(n-1): #row
        for j in range(len(grid[i])): #col, rev iter
            if grid[i][j] > grid[i+1][j]:
                return "NO"
    return "YES"

    # for i in range(n):
    #     grid[i] = sorted(grid[i])
    # for i in range(n-1):
    #     for j in range(n):
    #         if grid[i][j]>grid[i+1][j]:
    #             return "NO"
    # return "YES" 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(n, grid)

        fptr.write(result + '\n')

    fptr.close()
