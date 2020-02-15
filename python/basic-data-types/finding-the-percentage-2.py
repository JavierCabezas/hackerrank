from decimal import Decimal

number_of_students = int(input())
student_mark_dict = {}
for _ in range(0, number_of_students):
    unprocessed_data = input().split()
    student_name = unprocessed_data.pop(0)

    student_mark_dict[student_name] = list(map(float, unprocessed_data))

student_to_get_mark = input()
average = Decimal(sum(student_mark_dict[student_to_get_mark])/len(student_mark_dict[student_to_get_mark]))
print(round(average, 2))