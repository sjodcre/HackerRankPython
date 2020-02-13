# # Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for _ in range(n):
    value = input()
    print (bool(re.search(r"^([\+\-]?)([0-9]*)+\.([0-9]+)$", value)))
    # print(bool(re.search(r"^[+-]?[0-9]*\.[0-9]+$",value))  )   

# n = int(input())
# for _ in range(n):
#     s = input()
#     try:
#         int(s)
#         print(False)
#     except:
#         try:
#             float(s)
#             print(True)
#         except:
#             print(False)