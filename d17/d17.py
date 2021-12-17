import re

# assuming x1, x2 > 0, y1, y2 < 0
x1, x2, y1, y2 = map(int, re.search(r'x=(-*\d+)..(-*\d+), y=(-*\d+)..(-*\d+)', open('input.txt').read()).groups())
s = 0
ymx = -100000

for j in range(x2+1):
    # down abs(y1) to go directly from y = 0 to lowest y end coord
    # previous step was abs(y)-1
    # y coords are repeated when falling in y > 0, so initial vy = abs(y)-1 upper bound
    for i in range(y1, -y1):
        # simulation
        x, y = j, i
        st = 1
        while x <= x2 and y >= y1:
            if x1 <= x <= x2 and y1 <= y <= y2:
                s += 1
                break

            ymx = max(ymx, y)
            x += max(0, j-st)
            y += i-st
            st += 1

print('Star 1:', ymx)
print('Star 2:', s)
