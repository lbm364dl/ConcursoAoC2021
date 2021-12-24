# input program looks 14 times like this (only div, offset and add change):

#w input
#x = (z % 26) + offset != w
#z //= div
#z *= 25 * x + 1
#z += (add + w) * x

# div is only 1 or 26 (7 times each)
# when div == 1, 10 <= offset <= 15, x always True (w <= 9) (free to greedily choose w, max or min)
# then z = 26 * z + add + w, z has new digit in base 26
# then when div == 26 we always need to remove one digit to end with z == 0
# so only possible to set w = z % 26 + offset for x == 0 and no new digit (z = z * 1 + 0)

inp = open('input.txt').readlines()
div, offset, add = [[int(l.split()[-1]) for l in inp[pos::18]] for pos in [4, 5, 15]]

def sol(i, z, n, star2 = False):
    if i == 14:
        return n, True

    if div[i] == 26:
        w = z % 26 + offset[i]
        return sol(i + 1, z // 26, 10 * n + w, star2) if 1 <= w <= 9 else (-1, False)

    for d in sorted(range(1, 10), reverse = not star2):
        num, done = sol(i + 1, 26 * z + add[i] + d, 10 * n + d, star2)
        if done:
            return num, True

    return -1, False

print('Star 1:', sol(0, 0, 0)[0])
print('Star 2:', sol(0, 0, 0, star2 = True)[0])
