import numpy as np

grid = np.genfromtxt('input.txt', delimiter = 1, dtype = str)
n, m = grid.shape

its = 0
change = True
while change:
    change = False

    rows, cols = np.where((grid == '>') & (np.roll(grid, -1, 1) == '.'))
    grid[rows, (cols + 1) % m] = '>'
    grid[rows, cols] = '.'
    change |= rows.size > 0
    
    rows, cols = np.where((grid == 'v') & (np.roll(grid, -1, 0) == '.'))
    grid[(rows + 1) % n, cols] = 'v'
    grid[rows, cols] = '.'
    change |= rows.size > 0

    its += 1

print('Star 1:', its)
print('Star 2: no')
