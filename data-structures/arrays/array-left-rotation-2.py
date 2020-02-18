[number_of_elements, left_rotations] = [int(x) for x in input().split()]
rota_array = [int(x) for x in input().split()]

left_rotations =  left_rotations % number_of_elements
rotated_array = [
    rota_array[ ( number_of_elements + i + left_rotations ) % number_of_elements] for i in range(0, number_of_elements)
]

print(' '.join(map(str, rotated_array)))