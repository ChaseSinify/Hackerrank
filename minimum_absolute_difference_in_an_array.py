#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    a = sorted(arr)
    smallestGap = 10**9+1
    last = a[0]
    for i in range(1, len(a)):
        currentGap = abs(a[i] - last)
        if currentGap < smallestGap:
            smallestGap = currentGap
        last = a[i]
    return smallestGap

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
