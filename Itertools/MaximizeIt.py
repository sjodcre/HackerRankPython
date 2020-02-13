# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

x = input().split()
loops = int(x[0])
modul = int(x[1])
s=[]
for _ in range(loops):
    s.append(list(map(lambda x:x**2,map(int,input().split()[1:]))))
# print((s))
print(max([sum(i)%modul for i in product(*s)]))
