from itertools import permutations

s,n = input().split()
for x in sorted(list(permutations(s, int(n)))):
    print(*x, sep='')