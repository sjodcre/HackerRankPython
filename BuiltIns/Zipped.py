# Enter your code here. Read input from STDIN. Print output to STDOUT

noStu,noSub = map(int,input().split())
X = {}
for i in range(noSub):
    X[i]= list(map(float,input().split()))
print(*[sum(l)/len(l) for l in list(zip(*X.values()))],sep="\n")
# print(list(i) for i in zipp)
# print(i for i in zipp)
