from itertools import groupby
with open("rosalind_cons.txt") as f:
    groups = groupby(f, key=lambda x: not x.startswith(">"))
    d = {}
    for k,v in groups:
        if not k:
            key, val = list(v)[0].rstrip(), "".join(map(str.rstrip,next(groups)[1],""))
            d[key] = val
f.close()

l=len(d.values()[1])

bps={
"A":[0] * l,
"C":[0] * l,
"G":[0] * l,
"T":[0] * l,
}

for i in d.keys():
	for j in range(len(d[i])):
		bps[d[i][j]][j] += 1

consnum = []
for i in range(len(bps["A"])):
	consnum.append(bps["A"][i])

conslett = ""
for j in range(l):
	temp = "A"
	for i in range(1, 4):
		if bps.values()[i][j] > consnum[j]:
			consnum[j] = bps.values()[i][j]
			temp = bps.keys()[i]
	conslett += temp

print conslett

a = ""
for i in range(l):
	a += str(bps["A"][i]) + " "
print "A: " + a

c = ""
for i in range(l):
	c += str(bps["C"][i]) + " "
print "C: " + c

g=""
for i in range(l):
	g += str(bps["G"][i]) + " "
print "G: " + g

t=""
for i in range(l):
	t += str(bps["T"][i]) + " "
print "T: " + t








