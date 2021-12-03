def most_common(l, j):
    return int(2 * sum(l[i][j] for i in range(len(l))) >= len(l))

def iter(l, j, least = False):
    which = most_common(l, j) ^ least
    return [s for s in l if s[j] == which]

def to_int(l):
    return int(''.join(map(str,l)), 2)

def star1(inp):
    s = to_int([most_common(inp, j) for j in range(cols)])
    neg_s = (1 << cols) - 1 - s
    return s * neg_s

def star2(inp):
    nums_most, nums_least = inp.copy(), inp.copy()
    for j in range(cols):
        nums_most = iter(nums_most, j)
        nums_least = iter(nums_least, j, least = len(nums_least) > 1)

    return to_int(nums_most[0]) * to_int(nums_least[0])


inp = [[*map(int, line[:-1])] for line in open('input.txt')]
cols = len(inp[0])

print('Star 1:', star1(inp))
print('Star 2:', star2(inp))
