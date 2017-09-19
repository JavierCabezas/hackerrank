number_of_testcases = int(input())
cubes_lists = []
for _ in range(number_of_testcases):
    useless = input()
    cubes_lists.append(list(map(int, input().split(" "))))

def check(pile, initial_cube, last_cube):
    """
    :param pile:
    :param initial_cube:
    :param last_cube:
    :return:
         0: The last element of the pile is bigger than both initial and final elements of the cube
        -1: The first element of the cubes list should be removed
         1: The last element of the cubes list should be removed
    """
    if len(pile) > 0 and pile[-1] < initial_cube and pile[-1] < last_cube:
        return 0
    elif initial_cube > last_cube:
        return -1
    else:
        return 1

for cubes in cubes_lists:
    pile = []
    is_ok = True
    while len(cubes) > 0 and is_ok:
        response = check(pile, cubes[0], cubes[-1])
        if response == 0:
            is_ok = False
        else:
            if response == 1:
                to_add = cubes.pop()
            elif response == -1:
                to_add = cubes.pop(0)

            if len(pile) == 0 or to_add <= pile[-1]:
                pile.append(to_add)
            else:
                is_ok = False

    print( "Yes" if is_ok else "No")
