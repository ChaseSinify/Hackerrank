#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
#6x6:
#lowerbound i>0, we have to check i-1, but never j-1 
#upperbound i < 4, j < 4, last index to start at is arr[3][3]

def hourglassSum(arr):
    #the smallest possible value for arr[i][j] is -9, where we sum 7 total indexes;
    #therefore, the smallest value we need to init is -64, i.e. < -9 * 7
    ans = -64 
    for i in range(0, 4): #row/vertical
        for j in range(0, 4): #col/horizontal
            hg = [  
                    arr[i][j],      arr[i][j+1],    arr[i][j+2],
                                    arr[i+1][j+1],
                    arr[i+2][j],    arr[i+2][j+1],  arr[i+2][j+2]
                ]
            summy = sum(hg)
            if summy > ans:
                ans = summy
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
