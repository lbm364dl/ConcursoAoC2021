import re

# takes 3 secs

inp = [(op, *map(int,cs)) for op, *cs in re.findall(r'(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', open('input.txt').read())]
ops = [(op, i, [(x1, x2+1), (y1, y2+1), (z1, z2+1)]) for i, (op, x1, x2, y1, y2, z1, z2) in enumerate(inp)]

def volume(ops):
    if not ops:
        return 0
    if not ops[0][2]:
        # done with all coords, look for last op done on this area (1 if 'on' else 0)
        return max(ops, key = lambda x: x[1])[0] == 'on'

    # sweep line, iterate events (some region starts or ends)
    events = sorted((x, op, i, cs) for op, i, [xs, *cs] in ops for x in xs)
    # keep track of regions currently present at event
    sq = []
    using = set()
    vol = last = area = 0
    for x, op, i, cs in events:
        # vol == change in this dimension * change in smaller dimension
        vol += (x - last) * area
        # region ends
        if i in using:
            *sq, = filter(lambda p: p[1] != i, sq)
            using.remove(i)
        # region starts
        else:
            sq.append((op, i, cs))
            using.add(i)

        area = volume(sq)
        last = x

    return vol

print('Star 1:', volume(list(filter(lambda x: all(-50 <= c <= 50 for cs in x[2] for c in cs), ops))))
print('Star 2:', volume(ops))
