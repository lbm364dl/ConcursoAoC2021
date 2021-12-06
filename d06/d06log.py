import numpy as np

# matrix transformation with binary exponentiation approach O(logn) complexity
# fake complexity because of arbitrary size integers arithmetic (> linear in num digits)
# from 3e5 its approx answer has >1e4 digits
# still faster than the O(n) implementation from approx 2e5 its
# example for 4e6 its:
# other: 50s
# this: 27s

# dtype = object for arbitrary size integers
def bin_exp(A, n):
    M = np.eye(A.shape[0], dtype = object)
    while n > 0:
        if n&1:
            M = M.dot(A)
            n -= 1
        else:
            A = A.dot(A)
            n >>= 1

    return M

def ans(A, x0, its):
    return sum(bin_exp(A, its).dot(x0))

*inp, = map(int, open('input.txt').read().split(','))
# initial count
x0 = np.array([inp.count(i) for i in range(9)], dtype = object)
# transformation
A = np.array([
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0]
], dtype = object)

print('Star 1:', ans(A, x0, 80))
print('Star 2:', ans(A, x0, 256))
