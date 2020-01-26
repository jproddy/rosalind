import math
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

f = open("rosalind_indc.txt", "r")
s = f.read()
f.close()

n = int(s.strip())

p = math.pow(.5, 2*n)
print p

z = []

for i in range(1, 2*n+1):
	z.append(ncr(2*n, i))

for i in range(2 * n):
	z[i] += sum(z[i+1:2*n])

soln = []
for i in range(2 * n):
	soln.append(math.log10(z[i] * p))

print ' '.join(map(str, soln))




