import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

f = open("rosalind_lia.txt", "r")
s = f.read()
f.close()

slist = [int(x) for x in s.split(" ")]

# 0.25 probability a given person is AaBb
k = slist[0] # generation
N = slist[1] # num
z = []

for i in range(N, 2 ** k+1):
	z.append(ncr(2 ** k, i) * (.25 ** i) * (.75**(2**k - i)))

print sum(z)