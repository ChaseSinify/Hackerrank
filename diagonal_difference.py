#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    tlbr = 0 #top left -> bottom right
    bltr = 0 #bottom left -> top right
    for i in range(len(arr)):
        tlbr += arr[i][i]
    for i in range(len(arr)):
        bltr += arr[-(i+1)][i]
    return abs(tlbr - bltr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
