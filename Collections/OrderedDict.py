# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, price = input().rsplit(' ', 1)
    d[item] = d.get(item, 0) + int(price)
[print(item, d[item]) for item in d]
