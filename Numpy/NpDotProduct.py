import numpy
x = int(input())
A=[]
B=[]
for i in range(x):
    A.append(list(map(int,input().split())))
for i in range(x):
    B.append(list(map(int,input().split())))

print (numpy.dot(numpy.array(A), numpy.array(B)))
