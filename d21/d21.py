inp = [int(l.split()[-1])-1 for l in open('input.txt')]

def play(pos):
    n = turn = 0
    score = [0, 0]
    while score[turn^1] < 1000:
        pos[turn] = (pos[turn] + (n+3)*(n+4)//2 - n*(n+1)//2) % 10
        score[turn] += pos[turn] + 1
        n += 3
        turn ^= 1

    return n * score[turn]

# dict score from 3 rolls : occurrences of score
s = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
# memoization, save computed states
# number of states == pos * scores * turns == 10*10 * 22*22 * 2 < 1e5
# saving number of universes where each side wins, from this state
memo = {}
def wins(pl, sc, turn, uvs):
    if sc[0] >= 21:
        return uvs, 0
    if sc[1] >= 21:
        return 0, uvs
    if (pl, sc, turn) in memo:
        uvs0, uvs1 = memo[(pl, sc, turn)]
        # multiply by all universes from which we came
        return uvs0 * uvs, uvs1 * uvs

    tot = (0, 0)
    for res, cnt in s.items():
        pos = (pl[turn] + res) % 10
        score = sc[turn] + pos + 1
        new_pl = [(pos, pl[1]), (pl[0], pos)][turn]
        new_sc = [(score, sc[1]), (sc[0], score)][turn]
        cur1, cur2 = wins(new_pl, new_sc, turn ^ 1, uvs * cnt)
        tot = (tot[0] + cur1, tot[1] + cur2)

    # uvs from now == all / uvs until now
    memo[(pl, sc, turn)] = (tot[0]//uvs, tot[1]//uvs)
    return tot

print('Star 1:', play(inp.copy()))
print('Star 2:', max(wins(tuple(inp), (0, 0), 0, 1)))
