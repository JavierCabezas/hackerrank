useless = int(input())
numbers = list(map(int, input().split(" ")))
locations = {}

min_dif = len(numbers) + 1
for index, n in enumerate(numbers):
    if n in locations:
        dif = index - locations[n]
        min_dif = min(min_dif, dif)
    locations[n] = index

if min_dif == len(numbers) +1:
    min_dif = -1

print(min_dif)