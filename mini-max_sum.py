#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sumi = 0
    mini = 0
    maxi = 0
    for i in arr:
        sumi += i
    mini = sumi - (max(arr))
    maxi = sumi - (min(arr))
    print(mini, maxi)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
