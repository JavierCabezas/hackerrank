SELECT
CASE
    WHEN A+B <= C OR A+C <= B OR B+C <= A THEN
    'Not A Triangle'
    ELSE
        CASE
            WHEN A <> B AND B <> C AND A <> C THEN
              'Scalene'
            WHEN A = B AND A = C THEN
                'Equilateral'
            ELSE
                'Isosceles'
        END
    END
FROM triangles