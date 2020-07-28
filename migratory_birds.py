#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
"""
arr: an array of integers representing types of birds sighted 
"""
def migratoryBirds(arr):
    bins = [0]*6 #It is guaranteed that each type is 1, 2, 3, 4, or 5.
    for t in arr:
        bins[t] += 1

    return bins.index(max(bins))

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
