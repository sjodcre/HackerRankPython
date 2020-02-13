import numpy

n,m,p= map(int,input().split())
firstArr = numpy.array(list(map(int,input().split())))
# print(firstArr)
for _ in range(n+m-1):
    nextVal = numpy.array(list(map(int,input().split())))
    # print(nextVal)
#     numpy.concatenate(firstArr, nextVal)
    firstArr = numpy.concatenate((firstArr,nextVal))
print(firstArr.reshape(n+m,p))
