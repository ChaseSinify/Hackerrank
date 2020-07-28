#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    a = collections.Counter(s1)
    b = collections.Counter(s2)
    
    deletions = 0

    #base case, already anagrams
    if a == b:
        return 0
    else:
        # for k in a.keys():
        #     if k in b.keys():
        #         a[k] = abs(a[k] - b[k])
            
        for l in b.keys():
            if l in a.keys():
                a[l] = abs(a[l] - b[l])
            else:
                a[l] = b[l]

    for key in a.keys():
        deletions += a[key]
    
    return deletions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
