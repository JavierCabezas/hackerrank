import math

n = int(input())
groups = [list((map(int, input().split(" ")))) for _ in range(n)]
for g in groups:
    min_root = math.ceil(math.sqrt(g[0]))
    max_root = math.floor(math.sqrt(g[1]))
    if min_root > max_root:
        print(0)
    else:
        print(max_root - min_root + 1)