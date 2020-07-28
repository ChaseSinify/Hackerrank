#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    tree = 1 #starting at height 1, holds height of the tree
    for i in range(1, n+1):
        if i % 2 == 1:
            tree *= 2
        else:
            tree += 1
            
    return tree

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
