#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    # kang1 = [x1, v1]
    # kang2 = [x2, v2]
    flag = False
    if v1 == v2:
        if x1 == x2:
            flag = True
        else:
            flag = False
    elif v1 > v2:
        while(x1 <= x2):
            if x1 == x2:
                flag = True
            x1 += v1
            x2 += v2
    elif v2 > v1:
        while(x2 <= x1):
            if x1 == x2:
                flag = True
            x1 += v1
            x2 += v2
    if flag:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
