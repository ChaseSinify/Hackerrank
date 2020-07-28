#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the caesarCipher function below.
#NOTE: The cipher only encrypts letters; symbols, such as -, remain unencrypted. 
def caesarCipher(s, k): #s = string to rotate, k = rotation amount
    #NOTE: helpers for ascii shifting bounds
    #lower range: [97 - 122]
    #upper range: [65 - 90]
    #NOTE: 0 <= k <= 100
    ans = ""
    for c in range(len(s)):
        if (s[c] in string.ascii_lowercase): #lowercase letter
            temp = ord(s[c])
            temp += k
            if temp > 122: #if outside of lowercase, wrap around
                while temp > 122:
                    temp -= 26
            ans += chr(temp)
        elif (s[c] in string.ascii_uppercase): #uppercase letter
            temp = ord(s[c])
            temp += k
            if temp > 90: #if outside of lowercase, wrap around
                while temp > 90:
                    temp -= 26
            ans += chr(temp)
        else: #some char other than a letter, add this to string
            ans += s[c]
    return ans



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
