n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
a.sort()

min_found = abs(a[0] - a[1])
for i in range(len(a)-1):
    if abs(a[i] - a[i+1]) < min_found:
        min_found = abs(a[i] - a[i+1])
print(min_found)