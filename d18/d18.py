from functools import reduce

*inp, = map(eval, open('input.txt').readlines())
IGNORE, EXIT, NEED_ADD = -1, -2, -3

# performs the additions from explosion
def dir_add(t, is_right, add):
    if isinstance(t, int):
        return t + add
    elif is_right:
        return (t[0], dir_add(t[1], is_right, add))
    else:
        return (dir_add(t[0], is_right, add), t[1])

# after an explosion, add and then return until leaving function
def dfs(t, depth = 0):
    if isinstance(t, int):
        return t, IGNORE, IGNORE, IGNORE
    # explode
    if depth == 4:
        return 0, t[0], t[1], IGNORE

    newt0, t0, t1, add = dfs(t[0], depth+1)
    # just exploded, go add
    # closest right num is leftmost in t[1]
    # need to go back to find closest left num
    if t0 >= 0:
        return (newt0, dir_add(t[1], False, t1)), NEED_ADD, IGNORE, t0
    # go to the right to add to closest right regular number
    if t1 == NEED_ADD:
        return (newt0, dir_add(t[1], False, add)), EXIT, EXIT, EXIT
    # coming from left, can't go left, keep trying
    if t0 == NEED_ADD:
        return (newt0, t[1]), NEED_ADD, IGNORE, add
    # done adding, just leave
    if t0 == EXIT:
        return (newt0, t[1]), EXIT, EXIT, EXIT

    newt1, t0, t1, add = dfs(t[1], depth+1)
    # just exploded, go add
    # closest left num is rightmost in t[0]
    # need to go back to find closest right num
    if t0 >= 0:
        return (dir_add(t[0], True, t0), newt1), IGNORE, NEED_ADD, t1
    # go to the left to add to closest left regular number
    if t0 == NEED_ADD:
        return (dir_add(t[0], True, add), newt1), EXIT, EXIT, EXIT
    # coming from right, can't go right, keep trying
    if t1 == NEED_ADD:
        return (newt0, newt1), IGNORE, NEED_ADD, add
    # done adding, just leave
    if t1 == EXIT:
        return (newt0, newt1), EXIT, EXIT, EXIT

    return (newt0, newt1), IGNORE, IGNORE, IGNORE

def split(t):
    if isinstance(t, int):
        return [t, (t//2, (t+1)//2)][t >= 10], t >= 10

    newt0, found = split(t[0])
    if found:
        return (newt0, t[1]), True

    newt1, found = split(t[1])
    return (newt0, newt1), found

def magnitude(t):
    if isinstance(t, int):
        return t

    return 3 * magnitude(t[0]) + 2 * magnitude(t[1])

def reduce_num(t):
    while True:
        newt, _, _, _ = dfs(t)
        if newt == t:
            newt, _ = split(t)
            if newt == t:
                break

        t = newt

    return t

print('Star 1:', magnitude(reduce(lambda acc, x: reduce_num((acc, x)), inp)))
print('Star 2:', max(magnitude(reduce_num((n1, n2))) for n1 in inp for n2 in inp if n1 != n2))
