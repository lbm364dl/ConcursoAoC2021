inp = [[part.split() for part in l.split('|')] for l in open('input.txt')]

# segments that form each number in order from 0 to 9
segments = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
# letter c appears as segment in cnt[c] numbers
# {'a': 8, 'b': 6, 'c': 8, 'd': 7, 'e': 4, 'f': 9, 'g': 7}
cnt = {c : sum(c in entry for entry in segments) for c in 'abcdefg'}
# each number has a unique sum of cnt
# {42, 17, 34, 39, 30, 37, 41, 25, 49, 45}
to_num = {sum(cnt[c] for c in seg) : str(num) for num, seg in enumerate(segments)}

tot = 0
for entries, nums in inp:
    cnt = {c : sum(c in entry for entry in entries) for c in 'abcdefg'}
    # sums of cnt are just permuted
    # translate using the unique sum of cnt
    tot += int(''.join([to_num[sum(cnt[c] for c in num)] for num in nums]))

print('Star 1:', sum(len(num) in [2,3,4,7] for _, nums in inp for num in nums))
print('Star 2:', tot)
