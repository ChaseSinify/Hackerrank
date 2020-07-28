#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
"""
bill: an array of integers representing the cost of each item ordered
k: an integer representing the zero-based index of the item Anna doesn't eat
b: the amount of money that Anna contributed to the bill
"""
def bonAppetit(bill, k, b):
    temp = bill[:k] + bill[k+1:] #remove the item anna doesnt pay for
    if (sum(temp) // 2) == b:
        print("Bon Appetit")
    else:
        print(int(b - (sum(temp) / 2)))
        
    # return "Bon Appetit" if (sum(temp) / 2) == b else (sum(temp) / 2) - b

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
