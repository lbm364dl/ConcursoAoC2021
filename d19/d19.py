import numpy as np
from numpy.linalg import matrix_power
from collections import defaultdict

# very slow, takes 2 mins

inp = [np.array([[*map(int, p.split(','))] for p in sc.splitlines()[1:]]) for sc in open('input.txt').read().split('\n\n')]
n = len(inp)
left = set(range(1, n))
absolute = [inp[0], *[[] for i in range(1, n)]]
scan = [np.array([0, 0, 0]), *[[] for i in range(1, n)]]

ops = []
# clockwise 90deg rotation on yz plane (x fixed)
rot1 = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
# clockwise 90deg rotation on xz plane (y fixed)
rot2 = np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]])
# all orientations can be obtained as compositions of those two rotations
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                m = matrix_power(rot1, i).dot(matrix_power(rot2, j).dot(matrix_power(rot1, k).dot(matrix_power(rot2, l))))
                if not any((op == m).all() for op in ops):
                    ops.append(m)


def compare(i, j, q, left):
   cnt = defaultdict(int)
   for p1 in absolute[i]:
       for k in range(24):
           transformed = ops[k].dot(inp[j].transpose()).transpose()
           for p2 in transformed:
               cnt[tuple(p1-p2)] += 1

           for d, size in cnt.items():
               if size >= 12:
                   scan[j] = np.array(d, dtype = object)
                   absolute[j] = d + transformed
                   q.append(j)
                   left.remove(j)
                   return

# bfs on scanners with absolute position found
q = [0]
for i in q:
    for j in list(left):
        compare(i, j, q, left)

print('Star 1:', len({tuple(p) for ps in absolute for p in ps}))
print('Star 2:', max(sum(map(abs, scan[i]-scan[j])) for i in range(n) for j in range(i+1, n)))
