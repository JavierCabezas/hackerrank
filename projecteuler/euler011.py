#Project Euler #11: Largest product in a grid
row_max = 20
col_max = 20
adjacents = 4

matrix = []
def is_in_range(val, min_val, max_val):
    return val >= min_val and val <= max_val

def get_multiplication(neighbor):
    mult = 1
    for n in neighbor:
        r = n[0]
        c = n[1]
        if is_in_range(r, 0, row_max-1) and is_in_range(c, 0, col_max-1):
            mult *= matrix[n[0]][n[1]]
        else:
            mult *= 0
    return mult

def get_neighborhood(r, c):
    out = []
    out.append([(r-i, c) for i in range(adjacents)]) #down
    out.append([(r+i, c) for i in range(adjacents)]) #up
    out.append([(r, c-i) for i in range(adjacents)]) #left
    out.append([(r+i, c+i) for i in range(adjacents)]) #right
    out.append([(r-i, c-i) for i in range(adjacents)]) #diagonal down left
    out.append([(r-i, c+i) for i in range(adjacents)]) #diagonal up left
    out.append([(r+i, c-i) for i in range(adjacents)]) #diagonal down right
    out.append([(r+i, c+i) for i in range(adjacents)]) #diagonal up right

    return out


for _ in range(row_max):
    matrix.append(list(map(int, input().split(" "))))

max_mult = 0
for col in range(col_max):
    for row in range(row_max):
        for neighbor in get_neighborhood(row, col):
            temp_mult = get_multiplication(neighbor)
            if temp_mult > max_mult:
                max_mult = temp_mult

print(max_mult)