# Enter your code here. Read input from STDIN. Print output to STDOUT
i, m = input(), set(map(int, input().split()))
i, n = input(), set(map(int, input().split()))
diff = sorted(m.symmetric_difference(n))
print(*diff, sep ='\n')
