import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    # a = numpy.array(arr)
    # print(sorted(map(int,arr), key = lambda x: abs(x),reverse=True))
    return (numpy.array(sorted(map(float,arr), key = lambda x: abs(x),reverse=True),float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)