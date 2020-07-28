#!/bin/python3

import math
import os
import random
import re
import sys

# rtype: string (YES, NO)
"""
k: an integer
A: an array of integers
B: an array of integers
"""
def twoArrays(k, A, B):
    a = sorted(A)
    b = sorted(B)[::-1] #reverse as we are going to stack them
    for i in range(len(a)):
        if a[i] + b[i] < k:
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
