n_rows = int(input())
n_columns = int(input())
matrix = []

for _ in range(n_rows):
    matrix.append(list(map(int, input().split(" "))))

def is_in_range(val, min_val, max_val):
    return val >= min_val and val <= max_val

def get_neighborhood(r, c):
    return [[r_2, c_2] for r_2 in [r-1, r, r+1] for c_2 in [c-1, c, c+1] if is_in_range(r_2, 0, n_rows-1) and is_in_range(c_2, 0, n_columns-1) ]

def count_number_in_area(r, c):
    global matrix
    if matrix[r][c] == 0:
        return 0
    else:
        matrix[r][c] = 0
        total = 1
        for pair in get_neighborhood(r, c):
            total += count_number_in_area(pair[0], pair[1])
        return total

max_area = 0
for col in range(n_columns):
    for row in range(n_rows):
        temp = count_number_in_area(row, col)
        if temp > max_area:
            max_area = temp

print(max_area)