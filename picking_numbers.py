#!/bin/python3

import math
import os
import random
import re
import sys


# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
"""
a: an array of integers 
"""
def pickingNumbers(a):
    b = sorted(a)
    longest = 1
    for i in range(len(b)):
        j = 1
        temp = 1
        while i + j < len(b):
            if abs(b[i] - b[i+j]) <= 1:
                temp += 1
                if temp > longest:
                    longest = temp
            j += 1
    return longest
    # return longest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
