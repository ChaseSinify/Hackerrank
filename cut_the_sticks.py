#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    s = sorted(arr) #the smallest cut is always the left most, i index
    l = len(arr)
    ans = []
    if l == 1:
        return 1
    last = -1 #store the last seen element so we can ignore
    for i in range(l):
        if s[i] == last: #we already cut and removed these pces
            continue
        else:
            last = s[i]
        cuts = len(s[i:])
        ans.append(cuts)
    return ans


 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
