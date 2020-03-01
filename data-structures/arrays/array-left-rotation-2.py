def rotLeft(elements, number_of_rotations):
    number_of_elements = len(elements)
    new_starting_index = number_of_elements + number_of_rotations
    for _ in range(number_of_elements):
        print(elements[new_starting_index % number_of_elements], end=" ")
        new_starting_index += 1


nd = input().split()
number_of_elements = int(nd[0])
number_of_rotations = int(nd[1])

elements = list(map(int, input().rstrip().split()))
result = rotLeft(elements, number_of_rotations)
