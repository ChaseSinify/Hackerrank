#!/bin/python3

import os
import sys

#
# Complete the strangeGrid function below.
#
#NOTE: rows and cols are 1 indexed, but we dont really care for math
def strangeGrid(r, c):
    #row 1 starts as (row - 1) * 10 == 0: -> c * 2
    #if row % 2 == 0, its (row - 1) * 10 + 1 == 1: -> c * 2
    if r % 2 == 0: #
        rstart = ((r-2)*(10/2)) + 1

        #i.e. r = 3, rstart == ((3-1)*(10/2))
        #i.e. r = 4, rstart == ((4-2)*(10/2))+1

    else:
        rstart = ((r-1)*(10/2))
    return int(rstart + ((c-1)*2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rc = input().split()

    r = int(rc[0])

    c = int(rc[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
