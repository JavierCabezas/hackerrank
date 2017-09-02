number_of_testcases = int(input())
triangles = []
for _ in range(number_of_testcases):
    triangle_height = int(input())
    temp_triangle = []
    for _ in range(triangle_height):
        temp_triangle.append(list(map(int, input().split(" "))))
    triangles.append(temp_triangle)

for triangle in triangles:
    len_t = len(triangle)
    for row in range(len_t-1, 0, -1):
        for col in range(row):
            if triangle[row][col] > triangle[row][col+1]:
                triangle[row-1][col] += triangle[row][col]
            else:
                triangle[row-1][col] += triangle[row][col+1]
    print(triangle[0][0])