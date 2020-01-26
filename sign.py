from itertools import permutations
import numpy

f = open("rosalind_sign.txt", "r")
s = f.read()
f.close()

n = int(s.strip())

perm = permutations(range(1,n+1))
p = list(perm)

a = [1] * n + [-1] * n
aperm = list(permutations(a))
b = []
for i in aperm:
	if i[0:3] not in b:
		b.append(i[0:3])

print b
print p

sperm = []

for i in b:
	for j in p:
		ij = []
		for k in range(len(i)):
			ij.append(i[k]*j[k])
		sperm.append(ij)

print len(sperm)

for i in range(len(sperm)):
	print ' '.join(map(str, sperm[i]))