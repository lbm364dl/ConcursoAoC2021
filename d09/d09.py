grid = [[*map(int, l[:-1])] for l in open('input.txt')]
delta = [(1,0), (-1,0), (0,1), (0,-1)]
n, m = len(grid), len(grid[0])

def is_outside(y, x):
    return not (0 <= y < n and 0 <= x < m)

def is_low_point(y, x):
    return all(is_outside(y+dy, x+dx) or grid[y+dy][x+dx] > grid[y][x] for dy, dx in delta)

def dfs(y, x):
    if is_outside(y, x) or grid[y][x] == 9:
        return 0

    grid[y][x] = 9
    return 1 + sum(dfs(y+dy, x+dx) for dy, dx in delta)


lows = [(y, x, grid[y][x]) for y in range(n) for x in range(m) if is_low_point(y, x)]
b1, b2, b3 = sorted([dfs(y, x) for y, x, _ in lows])[-3:]

print('Star 1:', sum(val + 1 for _, _, val in lows))
print('Star 2:', b1 * b2 * b3)
