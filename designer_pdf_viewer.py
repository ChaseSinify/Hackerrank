#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
#NOTE: use ascii to get bin height of ord letter, max * length
def designerPdfViewer(h, word):
    lbound = 97 #ascii lowercase lowerbound for comparisons
    mx = 1
    for c in range(len(word)):
        if h[ord(word[c]) - lbound] == 7:
            mx = 7
            break
        elif h[ord(word[c]) - lbound] > mx:
            mx = h[ord(word[c]) - lbound]
    return mx * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
