len_array, number_of_rotations = map(int, input().split(" "))
initial_array = list(map(int, input().split(" ")))

shifted = [0] * len_array
c = len(initial_array) * number_of_rotations
for index, element in enumerate(initial_array):
    new_position = (index + c - number_of_rotations) % len_array
    shifted[new_position] = element

print(*shifted, sep=' ')