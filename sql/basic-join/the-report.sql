SELECT if(grades.grade < 8, NULL, name), grades.grade, students.marks
FROM students
JOIN grades ON marks BETWEEN min_mark AND max_mark
ORDER BY grade DESC, name ASC;