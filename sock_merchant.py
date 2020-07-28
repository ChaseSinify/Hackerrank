#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
"""
The first line contains an integer n, the number of socks represented in ar.
The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.
"""
def sockMerchant(n, ar):
    colors = [0] * 101 #100 is upperbound
    pairs = 0
    for color in ar:
        colors[color] += 1
    for colorBin in colors:
        if colorBin > 1:
            pairs += colorBin // 2

    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
