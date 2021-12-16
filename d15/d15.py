import heapq

# raw dijkstra is O(v^2 + e) v = nodes = n*m grid size, e = edges
# use priority queue to push and pop (get minimum cost) in O(logv)
# for dense graphs e close to v^2
# for sparse graphs e << v^2, few edges
# then O(vlogv + elogv) is more efficient
# a grid is a sparse graph (e < 4v)

INF = 1000000
grid = [[*map(int,l.strip())] for l in open('input.txt')]
n, m = len(grid), len(grid[0])

def solve(rep = 1):
    rn, rm = rep * n, rep * m
    cost = {(i, j) : INF for i in range(rn) for j in range(rm)}
    cost[(0,0)] = 0
    # priority queue
    pq = [(0, 0, 0)]
    heapq.heapify(pq)

    while pq:
        # top element is the min cost node
        c, i, j = heapq.heappop(pq)
        # ignore non optimal costs
        if c != cost[(i,j)]:
            continue

        if (i, j) == (rn-1, rm-1):
            return c

        for y, x in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= y < rn and 0 <= x < rm:
                # cool way to get value in grid
                val = (grid[y%n][x%m] + y//n + x//m -1) % 9 + 1
                if c + val < cost[(y,x)]:
                    cost[(y,x)] = c + val
                    heapq.heappush(pq, (cost[(y,x)], y, x))

    return INF

print('Star 1:', solve())
print('Star 2:', solve(5))
