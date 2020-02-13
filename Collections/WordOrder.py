# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

ops = int(input())
sets = OrderedCounter(input() for _ in range(ops))
print(len(sets))
print(*sets.values())

