import re

inp = re.findall(r'(\w)', open('input.txt').read())
inp = [(inp[i], inp[i+4]) for i in range(4)]
energy = {'A' : 1, 'B' : 10, 'C' : 100, 'D' : 1000}
end = {'A' : 2, 'B' : 4, 'C' : 6, 'D' : 8}
rooms = {2, 4, 6, 8}
hall = {0, 1, 3, 5, 7, 9, 10}
INF = 1000000

def in_correct_room(who, room):
    return all(c == ' ABCD'[room//2] for c in who[room])

def is_way_free(who, mn, mx):
    return not any(i in hall and who[i] for i in range(mn+1, mx))

def move(who, left, room_len, memo):
    if left == 0:
        return 0
    if tuple(who) in memo:
        return memo[tuple(who)]

    res = INF
    for i in range(11):
        if not who[i]: continue
        amph = who[i][0]
        if i in rooms and not in_correct_room(who, i):
            for j in hall:
                if who[j]: continue
                mn, mx = min(i, j), max(i, j)
                if is_way_free(who, mn, mx):
                    new_who = who.copy()
                    new_who[i] = new_who[i][1:]
                    new_who[j] = (amph,)
                    steps = mx - mn + room_len + 1 - len(who[i])
                    res = min(res, energy[amph] * steps + move(new_who, left, room_len, memo))
        elif i in hall:
            where = end[amph]
            mn, mx = min(i, where), max(i, where)
            if in_correct_room(who, where) and is_way_free(who, mn, mx):
                new_who = who.copy()
                new_who[i] = ()
                new_who[where] = who[where] + (amph,)
                steps = mx - mn + room_len - len(who[where])
                res = min(res, energy[amph] * steps + move(new_who, left-1, room_len, memo))

    memo[tuple(who)] = res
    return res

def least_energy(inp, star2 = False):
    if star2:
        inp = [(c1, c2, c3, c4) for (c1, c4), (c2, c3) in zip(inp, ['DD', 'CB', 'BA', 'AC'])]

    who = [inp[i//2-1] if i in rooms else () for i in range(11)]
    left = 0
    for cs, c in zip(inp, 'ABCD'):
        for cc in range(len(cs), 0, -1):
            if cs[cc-1] != c:
                left += cc
                break

    return move(who, left, len(inp[0]), {})

print('Star 1:', least_energy(inp))
print('Star 2:', least_energy(inp, star2 = True))
