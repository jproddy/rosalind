from itertools import groupby
with open("rosalind_kmer.txt") as f:
    groups = groupby(f, key=lambda x: not x.startswith(">"))
    d = {}
    for k,v in groups:
        if not k:
            key, val = list(v)[0].rstrip(), "".join(map(str.rstrip,next(groups)[1],""))
            d[key] = val
f.close()

s = d.values()[0]

from itertools import permutations

d = 4 # depth
a = ["A","C","G","T"] * d # alphabet * depth
perm = permutations(a,d)
p = list(perm)
p.sort()

r = []

for i in p:
	if i not in r:
		r.append(i)
qcount = [0] * len(r)
q = []

for i in r:
	temp = ""
	for j in range(len(i)):
		temp +=i [j]
	q.append(temp)


for i in range(len(s)-3):
	qcount[q.index(s[i:i+4])] += 1


print ' '.join(map(str, qcount))