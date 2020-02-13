import numpy
# numpy.set_printoptions(sign=' ')
numpy.set_printoptions(legacy='1.13')
n,m = map(int,input().split())
finalArr=[]
for _ in range(n):
    finalArr.append(list(map(int,input().split())))
print( numpy.mean(numpy.array(finalArr), axis = 1) )
print( numpy.var(numpy.array(finalArr), axis = 0) )
print( numpy.std(numpy.array(finalArr), axis = None) )

