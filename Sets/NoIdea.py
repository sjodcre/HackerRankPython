# Enter your code here. Read input from STDIN. Print output to STDOUT
a,test,setA,setB = input(),list(map(int,input().split())),set(map(int,input().split())),set(map(int,input().split()))
happiness = 0
for element in test:
    if element in setA:
        happiness+=1
    if element in setB:
        happiness-=1

print(happiness)
