# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

a, b = input().split()

[print("".join(i)) for x in range(1, int(b)+1) for i in combinations(sorted(a), x)]
