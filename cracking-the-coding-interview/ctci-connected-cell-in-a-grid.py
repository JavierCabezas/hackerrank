visited = {}

def getSumNearby(x, y):
    if x >= n_rows or x < 0:
        return 0
    if y >= n_cols or y < 0:
        return 0
    if grid[x][y] == 0:
        return 0

    if not x in visited:
        visited[x] = {}
    if not y in visited[x]:
        visited[x][y] = True
        total = grid[x][y]
        total += getSumNearby(x+1, y+1) # top right
        total += getSumNearby(x, y+1)   # top
        total += getSumNearby(x-1, y+1) # top left
        total += getSumNearby(x-1, y)   # middle left
        total += getSumNearby(x-1, y-1) # down left
        total += getSumNearby(x, y-1)   # down
        total += getSumNearby(x+1, y-1) # down right
        total += getSumNearby(x+1, y)   # middle right
        return total
    else:
        return 0 #already visited

def getBiggestRegion(n_rows, n_col):
    max_sum = 0
    for row in range(n_rows):
        for col in range(n_col):
            current_sum = getSumNearby(row, col)
            max_sum = max(current_sum, max_sum)
    return max_sum


n_rows = int(input().strip())
n_cols = int(input().strip())
grid = []
for grid_i in range(n_rows):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(n_rows, n_cols))

