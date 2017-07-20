n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
calories.sort(reverse=True)

total = 0
cupcake_index = 0
for c in calories:
    total += c*pow(2, cupcake_index)
    cupcake_index += 1
print(total)