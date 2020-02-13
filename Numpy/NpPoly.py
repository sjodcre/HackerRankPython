import numpy

p = numpy.array(list(map(float,input().split())))
x = int(input())
print (numpy.polyval(p, x))