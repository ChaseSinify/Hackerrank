#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m): #s = squares to consider, segment sum = d, segment length = m
    permutations = 0
    for i in range(len(s)):
        segsum = 0
        for x in s[i:i+m]:
            segsum += x
        if segsum == d:
            permutations += 1
    return permutations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
