# Enter your code here. Read input from STDIN. Print output to STDOUT
test = int(input())

for i in range(test):
    j,subsetA = input(),set(input().split())
    j,subsetB = input(),set(input().split())
    print(subsetA.issubset(subsetB))
