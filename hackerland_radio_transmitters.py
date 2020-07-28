#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the hackerlandRadioTransmitters function below.
# """
# x == amount of houses
# k == transmitter range
# """
# def hackerlandRadioTransmitters(x, k):
#     # #example 1, 2, 3, 4, 5 ; k = 1
#     # #expected 2 : [2, 4]
#     # transmitterRange = k #for easier to read vars
#     # sortedHouses = sorted(x) #sort for easier comparison and O time
#     # lastHouse = sortedHouses[0] #start with lastHouse location as first index house
#     # totalTransmitters = 0 #min size is 1, always need 1

#     # print(f'sortedHouses: {sortedHouses}')
#     # for house in range(1, len(sortedHouses)): #for each house number location
#     #     print(f'sortedHouse[house]: {sortedHouses[house]}')
#     #     print(f'lastHouse: {lastHouse}')
#     #     if sortedHouses[house] - lastHouse <= transmitterRange:
#     #         lastHouse = sortedHouses[house]
#     #     elif sortedHouses[house] - lastHouse > transmitterRange:
#     #         totalTransmitters +=1
#     #         #if this was our first transmitter
#     #         if lastHouse == sortedHouses[0]:
#     #             lastHouse = sortedHouses[house - 1] 
#     #         #for all others besides first
#     #         else:
#     #             lastHouse = sortedHouses[house]

#     #         print(f'UPDATED LAST HOUSE TO {lastHouse}')
#     #     print(f'totalTransmitters: {totalTransmitters}')
    
#     # if totalTransmitters == 0:
#     #     return 1
#     # else:
#     #     return totalTransmitters 

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     nk = input().split()

#     n = int(nk[0])

#     k = int(nk[1])

#     x = list(map(int, input().rstrip().split()))

#     result = hackerlandRadioTransmitters(x, k)

#     fptr.write(str(result) + '\n')

#     fptr.close()
#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]

x = sorted(x)
#logic
# 2 4 5 6 7 9 12
# Go as right as possible for first iteration
# Again go as right as possible for second iteration
# what does this mean that place transmitter in a such way that it will handle houses on left and right sides comfortably
# So first you are at left most position.. iterate over and find middle position where (middle-left==k) and then find right most position where (right-middle<=k)

count_trans = 0
last = x[0]
i = 0
while(i < n):
    count_trans = count_trans + 1
    next_point = x[i] + k
    while(i < n and x[i] <= next_point):
        i = i + 1
    next_point = x[i-1] + k
    while(i < n and x[i] <= next_point):
        i = i + 1

print(count_trans)
