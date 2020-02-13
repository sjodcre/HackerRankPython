# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
x = int(input())
# regex_num = r'^(?=([a-zA-Z]*(?:\d[a-zA-Z]*){3,}$))'
# regex_alpha = r'^(?=([a-z0-9]*(?:[A-Z][a-z0-9]*){2,}$))'
# https://stackoverflow.com/questions/51358885/regex-no-character-should-repeat
# https://stackoverflow.com/questions/10804732/what-is-the-difference-between-and-in-regex/10804791
regex_all = r'^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$'
for _ in range(x):
    num = bool(re.search(regex_all, input()))
    if num:
        print('Valid')
    else:
        print('Invalid')`