#!/bin/python3

import math
import os
import random
import re
import sys

#NOTE:
#for the three sides, its important that the sum of the smaller 2 is 
#strictly greater than the size of the math side
#we are looking for the largest values in the sorted array with this property
#Print the lengths of the
# chosen sticks as space-separated integers in non-decreasing order.
# If no non-degenerate triangle can be formed, print -1.
"""
sticks: an integer array that represents the lengths of sticks available
"""
def maximumPerimeterTriangle(sticks):
    stickies = sorted(sticks)
    
    #loop reverse over sorted; preference vs just reversing the sorted 
    for i in range(len(stickies)-1, 1, -1): #stop 2 early since we need i, i-1, i-2
        print(i)
        if stickies[i] < stickies[i-1] + stickies[i-2]:
            return [stickies[i-2], stickies[i-1], stickies[i]] 
    return [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
