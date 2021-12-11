import numpy as np

inp = np.array([[*map(int,l[:-1])] for l in open('input.txt')])
delta = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1, 1), (-1,-1)]
n, m = inp.shape
FLASH_LEVEL = 10

def dfs(x, y, grid, visited):
    if not (0 <= y < n and 0 <= x < m) or (x, y) in visited:
        return

    grid[y, x] += 1
    if grid[y, x] >= FLASH_LEVEL:
        visited.add((x, y))
        for dy, dx in delta:
            dfs(x+dx, y+dy, grid, visited)

def iter(inp, its = -1, sync = False):
    grid = np.copy(inp)
    s, i = 0, 1
    while True:
        grid += 1
        visited = set()
        for y, x in zip(*np.where(grid >= FLASH_LEVEL)):
            dfs(x, y, grid, visited)

        flash = grid >= FLASH_LEVEL
        s += flash.sum()

        if sync and flash.sum() == grid.size:
            return i
        if not sync and i == its:
            return s

        grid[flash] = 0
        i += 1

print('Star 1:', iter(inp, 100))
print('Star 2:', iter(inp, sync = True))
