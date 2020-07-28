#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
"""
scores: an array of integers 
"""
def breakingRecords(scores):
    #we dont consider init to be breaking a null record for either entry
    low = scores[0]
    high = scores[0]
    lowBreaks = 0
    highBreaks = 0
    for i in range(len(scores)):
        if scores[i] > high:
            high = scores[i]
            highBreaks += 1
        elif scores[i] < low:
            low = scores[i]
            lowBreaks += 1
        #it makes no difference to else test for same here
    return highBreaks, lowBreaks
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
