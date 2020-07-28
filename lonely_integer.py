#!/bin/python3

import math
import os
import random
import re
import sys
import operator
from functools import reduce

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    return reduce(int.__xor__,a)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
