#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    oddFlag = False #we can at most have 1 odd count, the center element
    passFlag = True
    c = collections.Counter(s)
    for k in c.keys():
        if c[k] % 2 != 0:
            if oddFlag == True: #if we already had an odd count
                passFlag = False
                break
            else:
                oddFlag = True
    return "YES" if passFlag else "NO"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
