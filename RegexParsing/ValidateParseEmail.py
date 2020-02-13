# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils

def fun(s):
    # return True if s is a valid email, else return False
    # regex = ^([a-zA-Z0-9_\-]+)@([a-zA-Z0-9]+)\.([a-zA-Z]{3})$
    # print(s)
    return bool(re.search(r"^[a-zA-Z][\w\-\.]+\@[a-zA-Z]+\.[a-zA-Z]{1,3}$", s))
    # return bool(re.search('[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}', s))
    
x = int(input())
for _ in range(x):
    x= email.utils.parseaddr(input())
    if fun(x[1]):
        print(email.utils.formataddr((x[0], x[1])))