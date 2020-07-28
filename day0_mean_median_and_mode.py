# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
from collections import Counter
from math import ceil

fptr = open(os.environ['OUTPUT_PATH'], 'w')
n = input().rstrip()
arr = list(map(int, input().rstrip().split()))
sorty = sorted(arr)
summy = sum(arr)
counties = Counter(arr)
print(counties)

#mean
mean = summy / len(arr)

#median logic:
if len(arr) % 2 == 0:
    median = (sorty[(len(sorty) // 2) - 1] + sorty[(ceil(len(sorty) / 2))]) / 2
else:
    median = sorty[len(sorty) // 2]

#mode via counting
mode = 0 #value count of most common number in arr
lastMode = 2**32-1 #to only return the "numerically smaller mode," per requirements
for i in counties:
    if counties[i] >= mode:
        mode = counties[i]
        if i < lastMode:
            lastMode = i


fptr.write(str(mean) + '\n')
fptr.write(str(median) + '\n')
fptr.write(str(lastMode) + '\n')

