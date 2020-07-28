#!/bin/python3

import math
import os
import random
import re
import sys

#Print a single integer that denotes the number of valleys Gary walked through during his hike.
# Complete the countingValleys function below.
"""
n: the number of steps Gary takes
s: a string describing his path
"""
def countingValleys(n, s):
    elevation = 0
    valleyCount = 0
    for i in range(n):
        if s[i] == 'U':
            elevation += 1
            if elevation == 0:
                valleyCount += 1

        elif s[i] == 'D':
            elevation -= 1

    return valleyCount
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
