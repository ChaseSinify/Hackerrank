#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    rev = s[::-1]
    flag = True
    for i in range(len(s) - 1):
        gap = abs(ord(s[i]) - ord(s[i+1]))
        revGap = abs(ord(rev[i]) - ord(rev[i+1]))
        if not gap == revGap:
            flag = False
            break
    return "Funny" if flag else "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
