#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    hr = "hackerrank"
    tracker = 0
    for i in range(len(s)):
        if s[i] == hr[tracker]:
            tracker += 1
        if tracker >= len(hr):
            break
    return "YES" if tracker >= len(hr) else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
