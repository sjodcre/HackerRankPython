# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S = input()
vowel = '[aeiou]'
consonant = '[qwrtypsdfghjklzxcvbnm]'
m = re.findall(r'{consonant}({vowel}{{2,}})(?={consonant})'.format(vowel=vowel, consonant=consonant), S, re.IGNORECASE)
if m:
        print(*m, sep='\n')
else:
    print(-1)	