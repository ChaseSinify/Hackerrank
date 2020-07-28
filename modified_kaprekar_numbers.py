#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    kn = ""
    for i in range(p, q+1):
        s = str(i * i)
        if len(s) > 1:
            h = int(len(s) / 2)
            if ( int(s[:h]) + int(s[h:]) ) == i:
                kn += str( int(s[:h]) + int(s[h:]) ) + " "
        elif int(s) == i:
                kn += s + " "
    
    if kn: print(kn)
    else: print("INVALID RANGE")
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
