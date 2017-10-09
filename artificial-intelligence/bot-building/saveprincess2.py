def display_path_to_princess(princess_pos, bot_pos):
    vertical = bot_pos[0] - princess_pos[0]
    horizontal = bot_pos[1] - princess_pos[1]

    vertical_text = "DOWN" if vertical > 0 else "UP"
    horizontal_text = "RIGHT" if horizontal > 0 else "LEFT"

    if abs(vertical) > 0:
        print(vertical_text)
    else:
        print(horizontal_text)


board_size = int(input())
useless = input()
for row_pos in range(board_size):
    row = input()

    try:
        col_pos = row.index('m')
        princess_pos = (row_pos, col_pos)
    except ValueError:
        pass

    try:
        col_pos = row.index('p')
        bot_pos = (row_pos, col_pos)
    except ValueError:
        pass

display_path_to_princess(princess_pos, bot_pos)


