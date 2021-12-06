def iter(its, inp):
    l = [inp.count(i) for i in range(9)]
    for _ in range(its):
        l = [l[(i+1)%9] for i in range(9)]
        l[6] += l[8]

    return sum(l)

*inp, = map(int, open('input.txt').read().split(','))
print('Star 1:', iter(80, inp))
print('Star 2:', iter(256, inp))
