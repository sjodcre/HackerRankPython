# Enter your code here. Read input from STDIN. Print output to STDOUT
unsorted_input = list(input())
print(*sorted(unsorted_input, key=lambda c: (c.isdigit() - c.islower(), str(int(c)%2==0 if c.isdigit() else c), c)), sep='')
# print(*sorted(unsorted_input, key=lambda c: (c.isdigit() - c.islower(), str(int(c)%2==0 if c.isdigit() else c), c)), sep='')
# key=lambda x:(not x.islower(), x)
# key=lambda c: c.lower() if c.isupper() else c.upper()
# for i in unsorted_input:
#     print(i.isdigit()-i.islower())
