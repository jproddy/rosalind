from itertools import groupby
with open("rosalind_gc.txt") as f:
    groups = groupby(f, key=lambda x: not x.startswith(">"))
    d = {}
    for k,v in groups:
        if not k:
            key, val = list(v)[0].rstrip(), "".join(map(str.rstrip,next(groups)[1],""))
            d[key] = val
f.close()
#print(d)

maxgcc = 0
maxname = ""
for i in d.keys():
	gcc = (d[i].count("G") + d[i].count("C")) / (1.0 * len(d[i]))
	if gcc > maxgcc:
		maxgcc = gcc
		maxname = i

print maxname
print maxgcc * 100
