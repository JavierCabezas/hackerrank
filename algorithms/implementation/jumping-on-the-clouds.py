number_of_elements = int(input())
clouds = [int(x) for x in input().split()]

GOOD_CLOUD = 0
BAD_CLOUD = 1

number_of_jumps = 0
current_position = 0
is_end_of_the_game = False

while True:
    can_jump_to_next_cloud = current_position + 1 < len(clouds) and clouds[current_position + 1] is GOOD_CLOUD
    can_jump_to_second_cloud = current_position + 2 < len(clouds) and clouds[current_position + 2] is GOOD_CLOUD
    is_end_of_the_game = not can_jump_to_next_cloud and not can_jump_to_second_cloud

    if can_jump_to_second_cloud:
        current_position += 2
        number_of_jumps += 1
    elif can_jump_to_next_cloud:
        current_position += 1
        number_of_jumps += 1
    elif is_end_of_the_game:
        break

print(number_of_jumps)
