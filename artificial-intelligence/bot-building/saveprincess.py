def displayPathtoPrincess(princess_pos, bot_pos):
    vertical = bot_pos[0] - princess_pos[0]
    horizontal = bot_pos[1] - princess_pos[1]

    vertical_text = "DOWN" if vertical > 0 else "UP"
    horizontal_text = "RIGHT" if horizontal > 0 else "LEFT"

    for _ in range(abs(vertical)):
        print(vertical_text)

    for _ in range(abs(horizontal)):
        print(horizontal_text)

maze_size = int(input())
princess_pos = (0, 0)
bot_pos = (0, 0)

for row_pos in range(0, maze_size):
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

displayPathtoPrincess(princess_pos, bot_pos)