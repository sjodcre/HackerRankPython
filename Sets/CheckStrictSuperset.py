# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(input().split())
conditions = int(input())
all_res = []
for i in range (conditions):
    setB = set(input().split())
    all_res.append(int(setA.issuperset(setB)))

if sum(all_res)!=conditions:
    print(False)
else:
    print(True)
