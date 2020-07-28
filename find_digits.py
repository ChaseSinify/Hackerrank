#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
"""
n: an integer to analyze
"""
def findDigits(n):
    ans = 0
    strnum = str(n)
    for i in range(len(strnum)):
        if strnum[i] != '0':
            if n % int(strnum[i]) == 0:
                ans += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
