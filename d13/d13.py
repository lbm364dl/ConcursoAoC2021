from functools import reduce
import numpy as np
import re

def fold(paper, instr):
    c, v = instr
    if c == 'x':
        return (paper[:,:v] | paper[:,:v:-1])[:,:v]
    elif c == 'y':
        return (paper[:v,:] | paper[:v:-1,:])[:v,:]

inp = open('input.txt').read()
folds = [(coord, int(val)) for coord, val in re.findall(r'([xy])=(\d+)', inp)]
ymax = max([(c == 'y')*v for c, v in folds])
xmax = max([(c == 'x')*v for c, v in folds])
x, y = zip(*[[*map(int, l)] for l in re.findall(r'(\d+),(\d+)', inp)])
paper = np.zeros((2*ymax+1, 2*xmax+1), dtype = object)
paper[y, x] = 1;

print('Star 1:', fold(paper, folds[0]).sum())
print('Star 2:')
print('\n'.join(''.join(' █'[c] for c in row) for row in reduce(fold, folds, paper)))
