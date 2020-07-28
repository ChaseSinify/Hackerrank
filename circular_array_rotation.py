#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
"""
a: an array of integers to rotate
k: an integer, the rotation count
queries: an array of integers, the indices to report
"""
def circularArrayRotation(a, k, queries):
    l = len(a)
    rot = k % l
    start = l - rot
    rotted = a[start:] + a[0:start]
    ret = []
    for q in queries:
        ret.append(rotted[q])
    return ret
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
