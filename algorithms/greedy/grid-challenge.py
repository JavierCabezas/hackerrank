def is_grid_ordered(grid):
    for i in range(len(grid)-1):
        for j in range(len(grid)):
            if grid[i][j] > grid[i+1][j]:
                return False
    return True

grids = []
for _ in range(int(input())):
    n_rows = int(input())
    grids.append([list(map(ord, input())) for __ in range(n_rows)])

for grid in grids:
    for row in grid:
        row.sort()
    if is_grid_ordered(grid):
        print('YES')
    else:
        print('NO')