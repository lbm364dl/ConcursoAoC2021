from collections import defaultdict

pos, im = open('input.txt').read().split('\n\n')
im = im.splitlines()
n, m = len(im), len(im[0])
im = defaultdict(lambda: '0', {(i, j) : '01'[col == '#'] for i, row in enumerate(im) for j, col in enumerate(row)})
pos = [x == '#' for x in pos]
delta = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]

def solve(its, im):
    for i in range(1, its+1):
        # in even iteration, use '1' as default
        cur = defaultdict(lambda: '10'[i&1])
        for y in range(-i, n+i):
            for x in range(-i, m+i):
                cur[(y, x)] = '01'[pos[int(''.join(im[(y+dy,x+dx)] for dy, dx in delta), 2)]]
    
        im = cur

    return sum(x == '1' for x in im.values())

print(solve(2, im))
print(solve(50, im))
