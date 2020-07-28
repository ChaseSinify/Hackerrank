#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    if n == 1:
        return 2
    liked = 0 #starts at day1, represents amount liked on day n
    summy = 0 #starts at day 1, represents total liked up to n (inclusive)
    shared = 5
    for i in range(n):
        liked = shared // 2
        shared = liked * 3
        summy += liked
    return summy
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
