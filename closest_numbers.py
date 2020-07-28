#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    a = sorted(arr)
    currDiff = 100000000000
    mins = []   

    for i in range(len(a) - 1):
        diff = abs(a[i] - a[i+1])
        if diff < currDiff:
            currDiff = diff
            mins = []
        if currDiff == diff:
            mins.append(a[i])
            mins.append(a[i+1])
    print(mins)
    return mins


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
