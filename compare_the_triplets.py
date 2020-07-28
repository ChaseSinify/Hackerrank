#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
"""
If a[i] > b[i], then Alice is awarded point.
If a[i] < b[i], then Bob is awarded point.
If a[i] = b[i], then neither person receives a point.

Your return array would be [1, 1] with Alice's score first and Bob's second. 
"""
def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]: alice += 1
        elif a[i] < b[i]: bob += 1
        elif a[i] == b[i]: continue
    return [alice, bob]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
