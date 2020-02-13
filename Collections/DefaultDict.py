# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = list(map(int,input().split()))
grpA = defaultdict(list)
for i in range(n):
    grpA[input()].append(i+1)
# print(grpA)
for i in range(m):
    curInp = input()
    if curInp in grpA.keys():
        print(*grpA[curInp])
    else:
        print('-1')
