# # Enter your code here. Read input from STDIN. Print output to STDOUT

import re
# x =int(input())
# for _ in range(x):
#     match = re.match(r'(?!^)(#[a-f0-9]{6}|[a-f0-9]{3})[^\n]', input(), re.IGNORECASE)
#     if match:
#         print(match)

for _ in range(int(input())):
    m = re.findall(r'(?!^)(#[a-f0-9]{6}|#[a-f0-9]{3})[^\n]', input(), re.IGNORECASE)
    if m:
        for s in m:
            print( s)