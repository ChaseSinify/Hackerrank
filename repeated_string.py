#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the repeatedString function below.
"""
The first line contains a single string, s.
The second line contains an integer, n.
"""
def repeatedString(s, n):
    return (s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
