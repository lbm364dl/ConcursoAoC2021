grid = [[*map(int, l[:-1])] for l in open('input.txt')]
delta = [(1,0), (-1,0), (0,1), (0,-1)]
n, m = len(grid), len(grid[0])

def is_outside(y, x):
    return not (0 <= y < n and 0 <= x < m)

def is_low_point(y, x):
    return all(is_outside(y+dy, x+dx) or grid[y+dy][x+dx] > grid[y][x] for dy, dx in delta)

def dfs(y, x):
    if is_outside(y, x) or grid[y][x] == 9 or (y,x) in visited:
        return 0

    visited.add((y, x))
    return 1 + sum(dfs(y+dy, x+dx) for dy, dx in delta)


lows = [(y, x) for y in range(n) for x in range(m) if is_low_point(y, x)]
visited = set()
basins = sorted([dfs(y, x) for y, x in lows])

print('Star 1:', sum(grid[y][x] + 1 for y, x in lows))
print('Star 2:', basins[-1] * basins[-2] * basins[-3])
