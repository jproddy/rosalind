from itertools import groupby
with open("rosalind_sseq.txt") as f:
    groups = groupby(f, key=lambda x: not x.startswith(">"))
    d = {}
    for k,v in groups:
        if not k:
            key, val = list(v)[0].rstrip(), "".join(map(str.rstrip,next(groups)[1],""))
            d[key] = val
f.close()

s = d.values()[1]		#full string
t = d.values()[0]		#substring
ind = []
# print s
# print t

tindex = 0

for i in range(len(s)):
	print i
	if s[i] == t[tindex]:
		ind.append(i+1)
		tindex += 1
	if tindex == len(t):
		break

# print ind
print ' '.join(map(str, ind))