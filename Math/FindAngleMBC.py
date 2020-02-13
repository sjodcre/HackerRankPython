import math
# Enter your code here. Read input from STDIN. Print output to STDOUT
AB,BC =int(input()),int(input())

# print(str(int(math.degrees(angle)+0.5))+'\u00b0')
# print(int(56.4999999+0.5))
print(str(round(math.degrees(math.atan2(AB, BC)))) + '°')
