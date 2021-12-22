import re
import numpy as np

# very slow, takes 7 mins

inp = re.findall(r'(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', open('input.txt').read())
# [a, b) semiopen intervals
ops = [(op, *[c + i%2 for i, c in enumerate(map(int, cs))]) for op, *cs in inp]
# coordinate compression
xs, ys, zs = [sorted({coord for op in ops for coord in op[i:i+2]}) for i in [1, 3, 5]]
# real coord to compressed coord
cx, cy, cz = [{x : i for i, x in enumerate(l)} for l in [xs, ys, zs]]
# real distances
dx, dy, dz = [[i2 - i1 for i2, i1 in zip(l[1:], l)] for l in [xs, ys, zs]]

def volume(ops):
    # 834*831*833 bytes approx 550MiB
    grid = np.zeros((len(xs), len(ys), len(zs)), dtype = bool)

    tot = 0
    for op, x1, x2, y1, y2, z1, z2 in ops:
        for x in range(cx[x1], cx[x2]):
            for y in range(cy[y1], cy[y2]):
                for z in range(cz[z1], cz[z2]):
                    if op == 'on':
                        if not grid[x][y][z]:
                            tot += dx[x] * dy[y] * dz[z]
                    else:
                        if grid[x][y][z]:
                            tot -= dx[x] * dy[y] * dz[z]

                    grid[x][y][z] = op == 'on'

    return tot

print('Star 1:', volume(list(filter(lambda x: all(-50 <= c <= 50 for c in x[1:]), ops))))
print('Star 2:', volume(ops))
