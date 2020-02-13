import numpy as np
n,m = map(int,input().split())
A=np.zeros((n,m),int)
B=np.zeros((n,m),int)
for i in range(n):
  A[i]=np.array(input().split(),int)
for i in range(n):
  B[i]=np.array(input().split(),int)  

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
