#!/bin/python3

import math
import os
import random
import re
import sys

"""
n: an integer representing Bobby's initial amount of money
c: an integer representing the cost of a chocolate bar
m: an integer representing the number of wrappers he can turn in for a free bar
"""
def chocolateFeast(n, c, m):
    bars = n // c #initial amount we buy with the money we had
    wrappers = bars #we have 1:1 wrappers for the bars we got thus far
    while wrappers >= m: #while we can turn in for at least 1 bar
        newbars = wrappers // m
        bars += newbars
        wrappers %= m #the wrappers we have now is the leftovers
        wrappers += newbars #add the new wrappers we got
    return bars

    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
