def iter(its, inp):
    d = {i : inp.count(i) for i in range(9)}
    for _ in range(its):
        d = {i : d[(i+1)%9] for i in range(9)}
        d[6] += d[8]

    return sum(d.values())

*inp, = map(int, open('input.txt').read().split(','))
print('Star 1:', iter(80, inp))
print('Star 2:', iter(256, inp))
