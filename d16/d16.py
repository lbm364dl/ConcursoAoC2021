from functools import reduce

inp = ''.join(f'{int(c, 16):04b}' for c in open('input.txt').read().strip())
f = [int.__add__, int.__mul__, min, max, None, int.__gt__, int.__lt__, int.__eq__]
v_sum = 0

def get_literal(l, x = '', bits = 0):
    if l[0] == '1':
        return get_literal(l[5:], x + l[1:5], bits + 5)
    else:
        return l[5:], bits+5, int(x + l[1:5], 2)

def parse_operator(l, op_type):
    bits = 1
    nums = []
    is_bits = l[0] == '0'
    stop, bits_len = [[12, 11], [16, 15]][is_bits]
    limit = int(l[1:stop], 2)
    l = l[stop:]
    bits += bits_len
    cnt = 0
    while cnt < limit:
        l, bs, res = parse(l)
        nums.append(res)
        bits += bs
        cnt += [1, bs][is_bits]

    return l, bits, reduce(f[op_type], nums)

def parse(l):
    global v_sum
    v_sum += int(l[:3], 2)
    t = int(l[3:6], 2)
    l, bits, res = get_literal(l[6:]) if t == 4 else parse_operator(l[6:], t)
    return l, 6 + bits, res

res = parse(inp)[2]
print('Star 1:', v_sum)
print('Star 2:', res)
