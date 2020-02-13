regex_pattern = r"^[789]{1}[0-9]{9}$"    # Do not delete 'r'.
# ^[7-9]\d{9}$
import re
x = int(input())
for _ in range(x):
    if bool(re.match(regex_pattern, input())) ==True:
        print('YES')
    else:
        print('NO')
# print(str(bool(re.match(regex_pattern, input()))))