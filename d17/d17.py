import re
from collections import defaultdict

x1, x2, y1, y2 = map(int, re.search(r'x=(-*\d+)..(-*\d+), y=(-*\d+)..(-*\d+)', open('ex').read()).groups())
x1, x2 = abs(x1), abs(x2)

mx = max(map(abs, [x1, x2, y1, y2]))
steps = defaultdict(list)
tr = defaultdict(list)
print(mx)

for i in range(mx+1):
    cur = i
    st = 1
    while cur <= mx and i > st:
        steps[cur].append((st, i-st+1, i))
        cur += i-st
        st += 1
    if i == st:
        tr[cur].append((st, i-st+1, i))

print(steps)
print(tr)
ans = 0
ps = []
for x in range(x1, x2+1):
    for y in range(-y2, -y1+1):
        #print(steps[x], steps[y])
        for sty, fromy, toy in steps[y]:
            for stx, fromx, tox in steps[x]:
                if fromx == 1:
                    if 2*(fromy-1)+1+sty >= stx:
                        ps.append((tox, fromy-1))
                    ans += 1
                elif stx == sty:
                    ps.append((tox, -fromy))
                    ans += 1
                elif 2*(fromy-1)+1+sty == stx:
                    ps.append((tox, fromy-1))
                    ans += 1


corr = sorted([(int(p1),int(p2)) for p1,p2 in re.findall(r'(\d+),(-*\d+)', open('pos').read())])
print(corr)

ps = sorted(set(ps))
print(ps)
print(len(ps))

print('ans', ans)
diff = set(corr)-set(ps)
print(diff, len(diff))
