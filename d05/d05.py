import re
import numpy as np

inp = [[*map(int, l)] for l in re.findall(r'(\d+),(\d+) -> (\d+),(\d+)\n', open('input.txt').read())]
n, m = 1000, 1000
grid = np.zeros((2, n, m))

for x1, y1, x2, y2 in inp:
    # swap points if needed to have x1 smaller
    if x1 > x2:
        (x1, y1), (x2, y2) = (x2, y2), (x1, y1)
    # vertical line
    if x1 == x2:
        grid[:, min(y1, y2):max(y1, y2)+1, x1] += 1
    # horizontal line
    elif y1 == y2:
        grid[:, y1, x1:x2+1] += 1
    # diagonal from (x1, y1) with x2-x1+1 elements
    elif y1 < y2:
        grid[1, y1:, x1:][np.diag_indices(x2-x1+1)] += 1
    # secondary diagonal from (x2, y2) with x2-x1+1 elements
    # diagonal of the counterclockwise 90deg rotated matrix
    elif y1 > y2:
        np.rot90(grid[1])[n-1-x2:, y2:][np.diag_indices(x2-x1+1)] += 1

print("Star 1:", (grid[0] >= 2).sum())
print("Star 2:", (grid[1] >= 2).sum())
