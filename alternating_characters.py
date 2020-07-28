#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    last = "" #store the last seen character
    deleteCount = 0 #store the amount of deletions required
    for i in range(len(s)):
        if last == "": #for our first iteration, init the last char to first seen
            last = s[i]
        else:
            if s[i] == last: #if current char same as last seen char
                deleteCount += 1
            else:
                last = s[i]
    return deleteCount



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
