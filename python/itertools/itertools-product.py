from itertools import product

a = tuple(map(int, input().split(" ")))
b = tuple(map(int, input().split(" ")))

print(*product(a,b), end=" ")