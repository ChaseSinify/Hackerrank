#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    counts = [0, 0, 0] #+, -, 0
    for i in arr:
        if i > 0:
            counts[0] += 1
        elif i < 0:
            counts[1] += 1
        else: #i == 0
            counts[2] += 1
            
    for i in counts:
        print(i / len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
