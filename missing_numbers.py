#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the missingNumbers function below.
"""
If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. If that is not the case, then it is also a missing number.
You have to print all the missing numbers in ascending order.
Print each missing number once, even if it is missing multiple times.
"""
#NOTE: arr: the array with missing numbers
#NOTE: brr: the original array of numbers 
def missingNumbers(arr, brr):
    a = Counter(arr)
    b = Counter(brr)
    missing = []
    for k in b.keys():
        if k not in a.keys(): #if num from b not in a, consider missing
            missing.append(k)
        elif b[k] > a[k]: #if there are more of this num in b than a, consider missing
            missing.append(k)
    return sorted(missing) #answer must be sorted

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
