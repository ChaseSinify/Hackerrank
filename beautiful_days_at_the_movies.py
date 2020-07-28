#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    # ans = 0
    # for day in range(i, j+1):
    #     d = str(day)
    #     r = d[::-1]
    #     a = abs(int(d) - int(r))
    #     if a % k == 0:
    #         ans += 1
    # return ans

    #one liner practice
    return sum([1 for day in range(i, j+1) if (day - int(str(day)[::-1])) % k == 0])
    # bd = [1 for day in range(i, j+1) if (day - int(str(day)[::-1])) % k == 0]
    # return sum(bd)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
