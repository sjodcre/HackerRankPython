# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

s = input().split()
string, number = sorted(s[0]), int(s[1])
# for x in list(itertools.combinations_with_replacement(string,number)):
#     print (''.join(x))
for i in range(1, number + 1):
    print (*list(map(''.join, itertools.combinations(string, i))),sep='\n')
