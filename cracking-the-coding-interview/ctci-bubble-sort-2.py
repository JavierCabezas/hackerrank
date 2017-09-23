n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

number_swaps = 0
for i in range(n-1):
    swaps_in_loop = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]
            swaps_in_loop += 1

    if swaps_in_loop == 0:
        break
    else:
        number_swaps += swaps_in_loop

print("Array is sorted in {0} swaps.".format(number_swaps))
print("First Element: {0}".format(a[0]))
print("Last Element: {0}".format(a[-1]))
