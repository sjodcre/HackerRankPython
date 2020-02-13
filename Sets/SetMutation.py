# Enter your code here. Read input from STDIN. Print output to STDOUT
i, m = input(),set(input().split())
j = int(input())

for ops in range(j):
    text = input().split()
    command = text[0]
    newset=set(input().split())
    if command == 'intersection_update':
        m.intersection_update(newset)
    if command == 'update':
        m.update(newset)
    if command == 'symmetric_difference_update':
        m.symmetric_difference_update(newset)
    if command == 'difference_update':
        m.difference_update(newset)

print(sum(list(map(int,m))))
# print(sum(x) for x in list(map(int,m)))
