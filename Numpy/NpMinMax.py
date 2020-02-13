import numpy

n,m = map(int,input().split())
finalArr =[]
for _ in range(n):
    finalArr.append(numpy.min(numpy.array(list(map(int,input().split())))))

print(numpy.max(numpy.array(finalArr)))