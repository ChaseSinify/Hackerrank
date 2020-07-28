#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password): #n = string length, password = password of n length 
    """Its length is at least 6
    It contains at least one digit.
    It contains at least one lowercase English character.
    It contains at least one uppercase English character.
    It contains at least one special character. The special characters are: !@#$%^&*()-+ 
    """
    # Return the minimum number of characters to make the password strong

    #NOTE: characters for comparisons from input
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    #flags for storing (bool) requirement info/state
    lenFlag = False
    numFlag = False
    lowerFlag = False
    upperFlag = False
    specialFlag = False
    length = n # store password length
    required = 0 #answer variable, how many chars we need to add

    #iterate password to check requirements
    for i in range(len(password)):
        if password[i] in numbers:
            numFlag = True
        if password[i] in lower_case:
            lowerFlag = True
        if password[i] in upper_case:
            upperFlag = True
        if password[i] in special_characters:
            specialFlag = True
        if i >= (6 - 1): #length requirement - 1 since index starting at 0
            lenFlag = True
    
    #add characters for each state flag missing
    if not numFlag:
        required += 1
        length += 1
    if not lowerFlag:
        required += 1
        length += 1
    if not upperFlag:
        required += 1
        length += 1
    if not specialFlag:
        required += 1
        length += 1
    if length < 6:
        required += (6 - length)
    
    return required



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
