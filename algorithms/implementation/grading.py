def solve(grades):
    for index, grade in enumerate(grades):
        if grade > 37 and grade % 5 >= 3:
            grades[index] += 5 - grade % 5
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))



