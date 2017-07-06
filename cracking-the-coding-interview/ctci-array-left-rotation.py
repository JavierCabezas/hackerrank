# in this problem im going to do the aproach of actually rotating the array instead of using a shortcut
# After all, the point of this is learning, right?
def array_left_rotation(array, number_of_rotations):
    arr_len = len(array)

    out = [None] * arr_len
    for i in range(arr_len):
        target_index = ( i + number_of_rotations ) % arr_len
        out[i] = array[target_index]

    return out

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, k)
print(*answer, sep=' ')
