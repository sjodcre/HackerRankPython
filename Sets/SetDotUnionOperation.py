# Enter your code here. Read input from STDIN. Print output to STDOUT
i, m = input(),set(input().split())
i, n= input(),set(input().split())
print(len(m.union(n)))
