from collections import namedtuple

n, Student = int(input()), namedtuple('Student', input())
total =sum([(int(Student(*input().split()).MARKS)) for i in range(n)])
print("{:.2f}".format(total/n))
# print("{:.2f}".format(sum([int(Student(*input().split()).MARKS) for _ in range(n)]) / n))
