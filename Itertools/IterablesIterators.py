
# import itertools
# n,s,number = input(), list(input().split()), int(input())
# total_list = list(itertools.combinations(s, number))
# a_list= (sum(map(int,('a' in s for s in total_list))))
# print(a_list/len(total_list))

n, number, k = int(input()), input().split().count('a'), int(input())
not_a = 1
for i in range(k):
    not_a = not_a * (n - number - i) / (n - i)
print(1-not_a)
