#!/bin/python3

import math
import os
import random
import re
import sys

"""
calorie: an integer array that represents calorie count for each cupcake
"""
def marcsCakewalk(calorie):
    sorty = sorted(calorie)[::-1]
    return sum(2**j * sorty[j] for j in range(len(sorty)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
