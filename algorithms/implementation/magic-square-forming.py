magic_square = []
for _ in range(3):
    for n in list(map(int, input().split(" "))):
        magic_square.append(n)

def get_sum(square, type):
    if type == 'top_row':
        return square[0] + square[1] + square[2]
    elif type == 'middle_row':
        return square[3] + square[4] + square[5]
    elif type == 'botom_row':
        return square[6] + square[7] + square[8]
    elif type == 'left_col':
        return square[0] + square[3] + square[6]
    elif type == 'middle_col':
        return square[1] + square[4] + square[7]
    elif type == 'right_col':
        return square[2] + square[5] + square[8]
    elif type == 'down_diag':
        return square[0] + square[4] + square[8]
    elif type == 'up_diag':
        return square[6] + square[4] + square[2]

def get_affected_sums(square_index):
    if square_index == 0:
        return ['top_row', 'left_col', 'down_diag']
    elif square_index == 1:
        return ['top_row', 'middle_col']
    elif square_index == 2:
        return ['top_row', 'right_col']
    elif square_index == 3:
        return ['left_col', 'middle_row', ]
    elif square_index == 4:
        return ['down_diag', 'up_diag', 'middle_row', 'middle_col']
    elif square_index == 5:
        return ['middle_row', 'right_col']
    elif square_index == 6:
        return ['left_col', 'bottom_row', 'up_diag']
    elif square_index == 7:
        return ['middle_col', 'bottom_row']
    elif square_index == 8:
        return ['right_col', 'bottom_row', 'down_diag']

def should_be_changed(matrix):
    to_be_changed = {}
    for index_to_test in range(9):
        to_be_changed[index_to_test] = True
        for type in get_affected_sums(index_to_test):
            if get_sum(matrix, type) == 15:
                to_be_changed[index_to_test] = False
    return to_be_changed

def squares():
    return [
            [8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4],
            [4, 9, 2, 3, 5, 7, 8, 1, 6], [2, 9, 4, 7, 5, 3, 6, 1, 8],
            [8, 3, 4, 1, 5, 9, 6, 7, 2], [4, 3, 8, 9, 5, 1, 2, 7, 6],
            [6, 7, 2, 1, 5, 9, 8, 3, 4], [2, 7, 6, 9, 5, 1, 4, 3, 8]
           ]

def get_cost(square_to_transform, result):
    cost = 0
    for i in range(9):
        cost += abs(square_to_transform[i] - result[i])
    return cost

min_cost = 1000
for square in squares():
    cost = get_cost(magic_square, square)
    if min_cost > cost:
        min_cost = cost
print(min_cost)