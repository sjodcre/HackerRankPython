import itertools

s = input().split()
string, number = sorted(s[0]), int(s[1])
# for x in list(itertools.combinations_with_replacement(string,number)):
#     print (''.join(x))
print (*list(map(''.join, itertools.combinations_with_replacement(string, number))),sep='\n')
