INDEX_GRADE = 1
INDEX_STUDENT = 0

number_of_elements = int(input())
student_grades = [[str(input()), float(input())] for _ in range(0, number_of_elements)]


# Sort by grade and then name
student_grades.sort(key=lambda x: (x[INDEX_GRADE], x[INDEX_STUDENT]))


# Use sets for getting an list with all the grades
all_grades = list(set([student_grade[INDEX_GRADE] for student_grade in student_grades]))
all_grades.sort()


# Get the second lowest grade and print the students with that grade
second_lowest = all_grades[1]
second_lowest_names = [student_grade[INDEX_STUDENT] for student_grade in student_grades if student_grade[INDEX_GRADE] == second_lowest]
print("\n".join(second_lowest_names))
