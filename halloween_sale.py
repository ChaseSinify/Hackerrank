#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
#p == initial game price
#d == price reduction per game bought
#m == price we continue until reached, then all items cost m
#s == the amounrt of money we start with
def howManyGames(p, d, m, s):
    games = 0
    while s >= p:
        games += 1
        s -= p
        p = max(p-d, m)
    return games
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
