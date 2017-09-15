from collections import namedtuple

n = int(input())
Student = namedtuple('Student', input())
marks = [Student(*(input().split())) for _ in range(n)]
print("{:.2f}".format(sum(float(p.MARKS) for p in marks)/n))