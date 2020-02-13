# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S,match = input(),input()
matches = re.finditer(r'(?=('+match+'))', S)
a = list(matches)
matches = iter(a)
for match in matches:
    print ((match.start(1), match.end(1) - 1))
if len(a) ==0:
    print ((-1, -1))
    
# m = re.findall(r'{match}'.format(match=match),S)
# print(*(mm.start(),mm.end()) for mm in m)