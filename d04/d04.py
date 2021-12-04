def row(used, i):
    return all(used[i][j] for j in range(m))

def col(used, j):
    return all(used[i][j] for i in range(n))

def winner(boards, places, last = False):
    # if last is the winner, compare time with >
    comp = [int.__lt__, int.__gt__][last]
    # trick to create independent lists using product (not having the same reference)
    used = eval(str([[[False] * m] * n] * len(boards)))
    # default time infinity for winner first, 0 for winner last
    time = 10000 * (not last)
    res = 0
    for use, place, board in zip(used, places, boards):
        for k, num in enumerate(nums):
            try:
                i, j = place[num]
                use[i][j] = True
                if row(use, i) or col(use, j):
                    if comp(k, time):
                        res = num * sum(board[i][j] for i in range(n) for j in range(m) if not use[i][j])
                        time = k
                    break
            except KeyError:
                pass

    return res

*inp, = open('input.txt')
*nums, = map(int, inp[0].split(','))
boards = [[[*map(int, line.split())] for line in inp[i:i+5]] for i in range(2, len(inp), 6)]
n, m = len(boards[0]), len(boards[0][0])
# dict number : position
places = [{board[i][j] : (i, j) for i in range(n) for j in range(m)} for board in boards]

print('Star 1:', winner(boards, places))
print('Star 2:', winner(boards, places, last = True))
