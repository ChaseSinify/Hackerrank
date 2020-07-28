#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the gemstones function below.
def gemstones(arr):
    gems = 0
    for c in string.ascii_lowercase:
        flag = True
        for w in range(len(arr)):
            if not c in arr[w]:
                flag = False
        if flag:
            gems += 1
                
    return gems

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
