is_board_clean = False

def get_closest_dirty_cell(posr, posc, board):
    min_dif = 25
    min_dif_pos_row = -1
    min_dif_pos_col = -1
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 'd':
                dif = abs(posr - r) + abs(posc - c)
                if dif < min_dif:
                    min_dif = dif
                    min_dif_pos_col = c
                    min_dif_pos_row = r
    return [min_dif_pos_row, min_dif_pos_col]


def next_move(bot_row, bot_col, board):
    global is_board_clean
    if board[bot_row][bot_col] == 'd':
        print('CLEAN')
        board[bot_row][bot_col] = '-'
    else:
        pos_next_dirty = get_closest_dirty_cell(bot_row, bot_col, board)
        dirty_row, dirty_col = pos_next_dirty[0], pos_next_dirty[1]
        if(dirty_row == -1):
            is_board_clean = True
        else:
            vertical = dirty_row - bot_row
            horizontal = dirty_col - bot_col

            if vertical > 0:
                print("DOWN")
                pos[0] += 1
            elif vertical < 0:
                print("UP")
                pos[0] -= 1
            elif horizontal > 0:
                print("RIGHT")
                pos[1] += 1
            elif horizontal < 0:
                print("LEFT")
                pos[1] -= 1


pos = [int(i) for i in input().strip().split()]
board = [[j for j in input().strip()] for i in range(5)]
while not is_board_clean:
    next_move(pos[0], pos[1], board)