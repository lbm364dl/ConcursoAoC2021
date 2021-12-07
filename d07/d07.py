*inp, = sorted(map(int, open('input.txt').read().split(',')))
print('Star 1:', sum(abs(inp[len(inp)//2] - x) for x in inp))
print('Star 2:', min(sum(abs(x-i)*-~abs(x-i)//2 for x in inp) for i in range(max(inp)+1)))
