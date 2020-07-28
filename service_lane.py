#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
"""
n: an integer denoting the size of the array
cases: a two dimensional array of integers where each element is an array of two integers representing starting and ending indices for a segment to consider . 
"""
def serviceLane(n, cases, width):
    ans = []
    for i in range(len(cases)):
        start, stop = cases[i]
        ans.append(min(width[start:stop+1]))
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases, width)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
