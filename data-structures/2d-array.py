#Calculates the hourglass sum given by the coordinates of the central element
#This function assumes that we give them the central elements of the array
def calculate_hourglass(x, y):
    return arr[y-1][x-1] + arr[y-1][x] + arr[y-1][x+1] + arr[y][x] + arr[y+1][x-1] + arr[y+1][x] + arr[y+1][x+1]

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

max_sum = calculate_hourglass(1, 1)
for x in range(1, 5):
    for y in range(1, 5):
        hourglass = calculate_hourglass(x, y)
        if hourglass > max_sum:
            max_sum = hourglass

print(max_sum)