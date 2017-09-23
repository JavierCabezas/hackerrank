from itertools import combinations

s,n = input().split()
for size in range(1, int(n)+1):
    for x in list(combinations(sorted(s), size)):
        print(*x, sep='')