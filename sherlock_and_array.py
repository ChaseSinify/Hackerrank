#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    t = sum(arr) #total sum of arr 
    s = 0 #store sums
    for i in range(len(arr)):
        cur = arr[i]
        t -= cur #remove the element we are looking at
        if s == t:
            return "YES"
        s += cur
    return "NO"

    # summy=sum(a)
    # l=len(a)
    # lefty=0
    # for i in range(len(a)):
    #     current=a[i]
    #     summy-=current
    #     if lefty==summy:
    #         return 'YES'
    #     lefty+=current
    # return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
