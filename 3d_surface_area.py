#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A, H, W):

    #start with the top and bottom areas, 1 for each
    area = 2 * H * W

    #padding -- add 0 arround the entire shape to not have to worry about out of bounds
    A.insert(0, [0] * len(A[0])) #top row pad
    A.insert(len(A), [0] * len(A[0])) #bottom row pad
    for i in range(len(A)):
        A[i].insert(0, 0) #left pad
        A[i].append(0) #right pad
    
    
    #for each cell in the 2D grid, take the area of that cell in full, then
    #remove the shared sides of all neighbors
    for i in range(1, H+1):
        for j in range(1, W+1):
            # area += A[i][j] * 4 #add the total area, note we already included top/bottom
            area += max(0, A[i][j] - A[i-1][j]) #top neighbor
            area += max(0, A[i][j] - A[i+1][j]) #bottom neighbor
            area += max(0, A[i][j] - A[i][j-1]) #left neighbor
            area += max(0, A[i][j] - A[i][j+1]) #right neighbor

    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A, H, W)

    fptr.write(str(result) + '\n')

    fptr.close()
