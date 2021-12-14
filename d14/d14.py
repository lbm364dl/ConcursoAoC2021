polymer, rules = open('input.txt').read().split('\n\n')
rules = dict([rule.split(' -> ') for rule in rules.splitlines()])

def iter(its):
    ps = {p : polymer.count(p) for p in rules}
    cnt = {c : polymer.count(c) for c in map(chr, range(ord('A'), ord('Z')+1))}
    for _ in range(its):
        for p, v in list(ps.items()):
            cnt[rules[p]] += v
            ps[p[0] + rules[p]] += v
            ps[rules[p] + p[1]] += v
            ps[p] -= v

    *cnt, = filter(None, cnt.values())
    return max(cnt) - min(cnt)

print('Star 1:', iter(10))
print('Star 2:', iter(40))
