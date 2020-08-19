from itertools import groupby
with open("rosalind_tran.txt") as f:
    groups = groupby(f, key=lambda x: not x.startswith(">"))
    d = {}
    for k,v in groups:
        if not k:
            key, val = list(v)[0].rstrip(), "".join(map(str.rstrip,next(groups)[1],""))
            d[key] = val
f.close()

s1 = d.values()[0]
s2 = d.values()[1]

pur = ["A","G"]
pyr = ["T","C"]
transitions = 0.0
transversions = 0.0

for i in range(len(s1)):
	if s1[i] != s2[i]:
		if (s1[i] in pur and s2[i] in pur) or (s1[i] in pyr and s2[i] in pyr):
			transitions += 1
		else:
			transversions += 1

print transitions / transversions