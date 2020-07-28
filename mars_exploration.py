#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    expected = "SOS"
    ans = 0
    for c in range(0, len(s), 3):
        temp = s[c:c+3]
        for x in range(len(expected)):
            if temp[x] != expected[x]:
                ans += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
