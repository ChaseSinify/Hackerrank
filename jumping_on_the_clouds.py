#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    moves = 0
    l = len(c)
    #NOTE: base cases
    if l == 1: #we are standing at the end already
        return 0
    elif l == 2 or l == 3: #in either case, we are 1 move from end assuming winnable
        return 1
    while i < (len(c)-1): #while not at end of array
        #since its assumed the game is winnable, we must be able to take
        #either 1 or 2 steps from any given index, thus, we move 2 whenever possible
        if i == l-2 or i == l-3:
            moves += 1
            break
        if c[i+2] == 1:
            i += 1
            moves += 1
        elif c[i+1] == 1:
            i += 2
            moves += 1
        else:
            i += 2
            moves += 1
        
    return moves
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
