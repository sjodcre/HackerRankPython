from collections import deque
d=deque()
ops = int(input())
for i in range(ops):
    inp = input().split()
    command = inp[0]
    values = inp[1:]
    execute = 'd.' + command + "(" + ",".join(values) + ")"
    eval(execute)
# Enter your code here. Read input from STDIN. Print output to STDOUT
print(*d)
