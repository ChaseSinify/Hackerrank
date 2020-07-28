#!/bin/python3

import math
import os
import random
import re
import sys

"""
n: an integer that denotes the number of chapters
k: an integer that denotes the maximum number of problems per page
arr: an array of integers that denote the number of problems in each chapter
"""
def workbook(n, k, arr):
    i = 0
    page = 1
    chapter = 1
    problem = 1
    turner = 0 #every k probs we turnm k == probs per page (unless last page in chap)
    special = 0 #1,1,1 will always be special
    while chapter <= n:
        probs = arr[i] #represents probs in arr[i] chapter, updated when we exhaust chap
        print(f'Chapter: {chapter}')
        #this loops per chapter
        for p in range(1, probs+1):
            print(f'Problem {problem} | Page: {page} | Turner: {turner} i: {i} p: {p}')
            if turner == k: #if we filled a page, turn to new one
                page += 1
                turner = 0 #reset after new page is made
            if problem == page:
                print(f'Special: chapter: {chapter} problem: {problem} page {page}')
                special += 1
            problem += 1 #we added new problem
            turner += 1 #we are 1 problem closer to new page
        
        #next chapter area
        if turner != 0: #if last page in chapter wasnt full
            page += 1 #new page for a chapter overrides turner
            turner = 0 #per above note, we need to reset this
        chapter += 1
        problem = 1 #reset for each chapter
        i += 1 #get the next chapters problem count from arr

    return special


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
