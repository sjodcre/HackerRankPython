# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
total = 0
nSize,sizes,nOrders = int(input()), Counter(map(int,input().split())), int(input())
for i in range(nOrders):
    size, price = map(int, input().split())
    if sizes[size]:
        total+=price
        sizes[size] -= 1
print(total)
