SELECT CONCAT(name, '(', LEFT(occupation, 1), ')')
FROM occupations
ORDER BY name;

SELECT CONCAT('There are total ', count(occupation), ' ', LOWER(occupation),  's.')
FROM occupations
GROUP BY occupation
ORDER BY count(*);