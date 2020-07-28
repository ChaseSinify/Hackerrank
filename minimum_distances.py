#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    mappy = {}
    smallest = -1
    for i in range(len(a)):
        if a[i] in mappy: #if this value exists as a key in our little mappy :3
            temp = i - mappy[a[i]] #calculate distance
            mappy[a[i]] = i #update the last seen position for this value
            if temp == 1:
                smallest = 1
                break
            elif smallest == -1:
                smallest = temp
            elif temp < smallest:
                smallest = temp
        else:
            mappy[a[i]] = i #if not in mappy, insert it :)
    return smallest
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
