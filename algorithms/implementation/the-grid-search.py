def is_word_in_row(word, row, col):
    '''
    This method checks if the word given by params is on the row
    :param word: word to find
    :param row: row matrix in where we are going to look for the word
    :param col: The column in where the last word was found. In case its given then the next word must be on the same column, otherwise we didn't find the word.
    In case its -1 it means that we don't know the column value yet so we are setting a new one.
    :return:
    '''
    try:
        col_pos = row.index(word)
        if col is -1:
            return col_pos #Set new column value since we didn't had an old one.
        else:
            if col_pos == col:
                return col_pos #Everything its OK. The word was found and it starts on the same column.
            else:
                return -1 #Word found but not on the same column
    except ValueError:
        return -1


def check_matrix(big_matrix, to_find):
    for row_idx_to_check in range(len(big_matrix) - len(to_find)):
        idx_to_find = 0
        found_in_what_col = -1
        for idx_offset in range(len(to_find)):
            found_in_what_col = is_word_in_row(to_find[idx_to_find], big_matrix[row_idx_to_check + idx_to_find], found_in_what_col)
            if found_in_what_col > 0:
                idx_to_find += 1
            if len(to_find) == idx_to_find:
                return True

    return False  # Saw all the elements in the matrix without success


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