from functools import reduce

inp = open('input.txt').read().splitlines()
open_to_close = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}
score1 = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
score2 = {'(' : 1, '[' : 2, '{' : 3, '<' : 4}

def score(l, stack, corrupted = True):
    if not l:
        return (not corrupted) * reduce(lambda x, y: 5*x + score2[y], stack[::-1], 0)
    elif l[0] in open_to_close:
        return score(l[1:], [*stack, l[0]], corrupted)
    elif open_to_close[stack[-1]] == l[0]:
        return score(l[1:], stack[:-1], corrupted)
    else:
        return corrupted * score1[l[0]]

scores2 = sorted(filter(None, [score(l, [], False) for l in inp]))
print('Star 1:', sum(score(l, []) for l in inp))
print('Star 2:', scores2[len(scores2)//2])
