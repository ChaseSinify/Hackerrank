#!/bin/python3

import os
import sys


# Complete the pageCount function below.
"""
n: the number of pages in the book
p: the page number to turn to
"""
def pageCount(n, p):
    # ftb = n // 2 #max moves from start -> end or end -> start linear traversal
    # ftp = p // 2 #moves from front of the book to page p
    # btp = ftb - ftp #moves from back of the book to page p
    # return min(ftp, btp)
    return min(p//2, n//2 - p//2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
