#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    aCount = 0 #apples that fall on house
    oCount = 0 #oranges that fall on house
    #assuming it is implied there is disjoint space set for tree locations and house
    #i.e. trees are not inside the house...
    #apple falls on house if d >= s - a and d <= t - a
    #orange falls on house if d<0, |d| >= b - t and |d| <= b - s
    for apl in range(len(apples)):
        if apples[apl] >= (s - a): 
            if apples[apl] <= (t - a): 
                aCount += 1

    for orng in range(len(oranges)):
        if (oranges[orng] < 0): 
            if (abs(oranges[orng]) >= (b - t)):
                if(abs(oranges[orng]) <= (b - s)):
                    oCount += 1

    print(aCount)
    print(oCount)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
