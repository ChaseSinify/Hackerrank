import os

fptr = open(os.environ['OUTPUT_PATH'], 'w')
n = int(input()) #num of elements in each array x, w
x = list(map(int, input().rstrip().split())) #arr; elements of x
w = list(map(int, input().rstrip().split())) #arr; represents weights of x elements

#calculate weighted mean
summy = 0
wsum = 0
for i in range(n):
    summy += x[i] * w[i]
    wsum += w[i]

fptr.write(str(round(summy / wsum, 1)) + '\n')
fptr.close()
