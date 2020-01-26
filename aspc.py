import operator as op
from functools import reduce

f = open("rosalind_aspc.txt", "r")
s = f.read()
f.close()

slist = [int(x) for x in s.split(" ")]

n = slist[0]
m = slist[1]


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


s = 0

for k in range(m, n+1):
	s += ncr(n, k)
	s = s % 1000000

print s