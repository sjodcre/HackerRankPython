# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
x = int(input())
regex_all = r'^([4-6]\d{3}\-?\d{4}\-?\d{4}\-?\d{4}$)'
for _ in range(x):
    num = re.search(regex_all, input())
    if num:
        processed_string = "".join(num.group(0).split('-'))
        final_match = re.search(r'(\d)\1{3,}',processed_string)
        print ('Invalid' if final_match else 'Valid')
    else:
        print('Invalid')