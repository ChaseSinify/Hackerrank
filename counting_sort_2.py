#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    countarr = [0] * 100
    sorter = []
    for i in arr:
        countarr[i] += 1
    for j in range(len(countarr)):
        if countarr[j] > 0:
            for x in range(countarr[j]):
                sorter.append(j)
    return sorter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
