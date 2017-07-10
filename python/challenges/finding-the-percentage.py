from decimal import Decimal

def print_percentage(grades, person):
    if person in grades:
        if len(grades[person]) > 0:
            average = Decimal(sum(grades[person])/len(grades[person]))
            print(round(average, 2))

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

print_percentage(student_marks, query_name)