import numpy
n,m = map(int,input().split())
my_array = []
for _ in range(n):
    my_array.append(list(map(int,input().split())))
my_array = numpy.array(my_array)
print(numpy.transpose(my_array))
print(my_array.flatten())

