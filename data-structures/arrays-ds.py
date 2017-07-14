n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr_lenght = len(arr) - 1

for x in range(0, arr_lenght + 1):
    print(arr[arr_lenght-x], end=' ')
