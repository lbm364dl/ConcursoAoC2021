import re
from copy import deepcopy
import numpy as np
from numpy.linalg import matrix_power
from collections import defaultdict

inp = [np.array([[*map(int, l.split(','))] for l in scanner.strip().splitlines()], dtype = object) for scanner in re.split(r'--- scanner \d+ ---', open('input.txt').read())[1:]]
n = len(inp)

done = {0}
absolute = {i : [] for i in range(n)}
absolute[0] = inp[0]
scanners = {0 : np.array([0,0,0])}

ops = []
# clockwise 90deg rotation on yz plane (x fixed)
rot1 = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]], dtype = object)
# clockwise 90deg rotation on xz plane (y fixed)
rot2 = np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]], dtype = object)

for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                m = matrix_power(rot1, i).dot(matrix_power(rot2, j).dot(matrix_power(rot1, k).dot(matrix_power(rot2, l))))
                if not any((op == m).all() for op in ops):
                    ops.append(m)

def transform(i, ps):
    return np.array([ops[i].dot(p) for p in ps])

q = {0}
while len(done) < n:
    i = q.pop()
    print(done, i, q)
    for j in range(n):
        if j in done:
            continue

        found = False
        cnt = defaultdict(int)
        for p1 in absolute[i]:
            for k in range(24):
                transformed = transform(k, inp[j])
#                print(transformed)
                for p2 in transformed:
                    cnt[tuple(p1-p2)] += 1
#                if j == 1:
#                    print([cnt[k] for k in cnt if cnt[k] > 1])
                for d, size in cnt.items():
                    if size >= 12:
                        scanners[j] = d
                        absolute[j] = d + transformed
                        q.add(j)
                        done.add(j)
                        found = True
                        break
                if found: break
            if found: break

s = set()
for k in done:
    for p in absolute[k]:
        s.add(tuple(p))

def manhattan(p1, p2):
    return sum(abs(p1[i]-p2[i]) for i in range(3))

print(max(manhattan(scanners[i], scanners[j]) for i in range(n) for j in range(i+1, n)))
print(len(s))
#print({tuple(p) for ps in absolute for p in ps})

