# Enter your code here. Read input from STDIN. Print output to STDOUT
n, numList = int(input()),list(map(int,input().split()))
print(any(str(x) == str(x)[::-1] for x in numList if all(x>=0 for x in numList)))
# str(test_number) == str(test_number)[::-1] # print(numList)
