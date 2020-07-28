#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    temp = ""
    entryLength = 0
    exitLength = 0
    while len(s) > 1: #string length of 1 is max reduced, 0 returns empty string 
        entryLength = len(s)
        for c in range(len(s) - 1):
            if s[c] == s[c+1]:
                temp = s[:c] + s[c+2:]
                exitLength = len(temp)
        
        #if there was nothing left to delete (all unique chars)
        if entryLength == exitLength:
            break

        s = temp

    if s == "":
        return "Empty String"
    else:
        return s
    # i = 3
    # test = "aaabccddd"
    # print(test)
    # print(test[:i] + test[i+2:])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
