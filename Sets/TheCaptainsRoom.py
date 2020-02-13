# Enter your code here. Read input from STDIN. Print output to STDOUT
i,m = int(input()),list(map(int,input().split()))
cap_room = (sum(set(m))*i - sum(m))//(i-1)
print(cap_room)
