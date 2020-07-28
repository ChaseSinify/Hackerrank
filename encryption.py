#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    sr=s.replace(" ","")
    row = math.floor(math.sqrt(len(sr)))
    col = math.ceil(math.sqrt(len(sr)))
    temp = ""
    for i in range(col):
        temp += sr[i::col] + " "
    return temp
    # s=input()
    # sm=s.replace(" ","")
    # r=math.floor(math.sqrt(len(sm)))
    # c=math.ceil(math.sqrt(len(sm)))
    # for i in range(c):
    #     print(sm[i::c],end=" ")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
