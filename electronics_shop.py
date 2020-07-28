#!/bin/python3

import os
import sys

"""
keyboards: an array of integers representing keyboard prices
drives: an array of integers representing drive prices
b: the units of currency in Monica's budget
"""
def getMoneySpent(keyboards, drives, b):
    ans = 0
    for k in range(len(keyboards)):
        for d in range(len(drives)):
            if keyboards[k] + drives[d] > ans and keyboards[k] + drives[d] <= b:
                ans = keyboards[k] + drives[d]
    return ans if ans else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
