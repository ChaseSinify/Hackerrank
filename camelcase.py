#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the camelcase function below.
def camelcase(s):
    if s == '':
        return 0
    ans = 1
    for c in s:
        if c in string.ascii_uppercase:
            ans += 1
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
