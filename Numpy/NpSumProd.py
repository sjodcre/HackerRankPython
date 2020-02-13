import numpy
n,m = map(int,input().split())
arr = numpy.zeros((n,m),int)
for i in range(n):
    arr[i] = numpy.array(input().split(),int)
print(numpy.prod(numpy.sum(arr, axis = 0)))