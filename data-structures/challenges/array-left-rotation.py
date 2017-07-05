n, number_of_rotations = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
arr_len = len(arr)

#Using the splice operator would be way to easy
number_of_rotations = number_of_rotations % arr_len

for i in range(0, arr_len):
    index = (arr_len + i + number_of_rotations ) % arr_len #We assure that we don't get negatives
    print(arr[index], end=' ')