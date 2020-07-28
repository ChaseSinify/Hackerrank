#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the pangrams function below.
def pangrams(s):
    flag = True
    for letter in string.ascii_lowercase:
        if letter not in s.lower():
            flag = False
    return "pangram" if flag else "not pangram"          

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
