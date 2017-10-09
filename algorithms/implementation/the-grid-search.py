def check_if_all_are_equal(matrix, to_find, n_row, n_col):
    rows_to_find = len(to_find)
    cols_to_find = len(to_find[0])

    for row_offset in range(rows_to_find):
        for col_offset in range(cols_to_find):
            if matrix[n_row + row_offset][n_col + col_offset] != to_find[row_offset][col_offset]:
                return False
    return True

def check_matrix(matrix, to_find):
    n_rows = len(matrix) - len(to_find) + 1
    n_cols = len(matrix[0]) - len(to_find[0]) + 1

    for n_row in range(n_rows):
        for n_col in range(n_cols):
            if matrix[n_row][n_col] == to_find[0][0]:
                if check_if_all_are_equal(matrix, to_find, n_row, n_col):
                    return True

    return False


number_of_testcases = int(input())
matrixes = [] #Array with the matrixes
to_find = []  #Array with the items to find. They share the index with the matrixes array

for _ in range(number_of_testcases): #Fill both arrays
    new_matrix = []
    new_to_find = []
    n_row, n_col = input().split(" ")
    for _ in range(int(n_row)):
        new_matrix.append(input())

    n_row_to_find, n_col_to_find = input().split(" ")
    for _ in range(int(n_row_to_find)):
        new_to_find.append(input())

    matrixes.append(new_matrix)
    to_find.append(new_to_find)


for idx, matrix in enumerate(matrixes):
    print("YES" if check_matrix(matrix, to_find[idx]) else "NO")