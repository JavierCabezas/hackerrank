number_of_elements = int(input().strip())
target_array = list(map(int, input().strip().split(' ')))
target_array.sort()

min_found = abs(target_array[0] - target_array[1])
for i in range(1, len(target_array)-1):
    min_found = min(min_found, abs(target_array[i] - target_array[i+1]))
print(min_found)