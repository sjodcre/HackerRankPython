# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
x = complex(input())
a= x.real
b= x.imag
print(math.hypot(a,b))
print(math.atan2(b,a))
