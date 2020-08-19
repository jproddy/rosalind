from itertools import groupby
with open("rosalind_grph.txt") as f:
    groups = groupby(f, key=lambda x: not x.startswith(">"))
    d = {}
    for k,v in groups:
        if not k:
            key, val = list(v)[0].rstrip(), "".join(map(str.rstrip,next(groups)[1],""))
            d[key] = val
f.close()

for i in d.keys():
	for j in d.keys():
		if i != j:
			l = len(d[i])
			if(d[i][l-3:] == d[j][:3]):
				print i[1:] + " " + j[1:]