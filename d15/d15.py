import heapq

# raw dijkstra is O(v^2 + e) v = nodes = n*m grid size, e = edges
# use priority queue to push and pop (get minimum cost) in O(logv)
# for dense graphs e close to v^2
# for sparse graphs e << v^2, few edges
# then O(vlogv + elogv) is more efficient
# a grid is a sparse graph (e < 4v)

INF = 1000000
grid = [[*map(int,l[:-1])] for l in open('input.txt')]
n, m = len(grid), len(grid[0])

def solve(rep = 1):
    cost = {(i, j) : INF for i in range(rep*n) for j in range(rep*m)}
    cost[(0,0)] = 0
    left = {(i, j) for i in range(rep*n) for j in range(rep*m)}
    # priority queue
    pq = [(INF, i, j) for i in range(rep*n) for j in range(rep*m)]
    pq[0] = (0, 0, 0)
    heapq.heapify(pq)

    while pq:
        # heap top element is the min cost node
        c, i, j = heapq.heappop(pq)
        if c != cost[(i,j)]: continue
        if (i, j) == (rep*n-1, rep*m-1):
            return cost[(i, j)]

        left.remove((i, j))
        for ny, nx in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if not (ny, nx) in left: continue
            # cool way to get value in grid
            val = (grid[ny%n][nx%m] + ny//n + nx//m -1) % 9 + 1
            if c + val < cost[(ny,nx)]:
                cost[(ny,nx)] = c + val
                heapq.heappush(pq, (cost[(ny,nx)], ny, nx))

    return INF

print('Star 1:', solve())
print('Star 2:', solve(5))
