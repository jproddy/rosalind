from itertools import groupby
with open("rosalind_revp.txt") as f:
    groups = groupby(f, key=lambda x: not x.startswith(">"))
    d = {}
    for k,v in groups:
        if not k:
            key, val = list(v)[0].rstrip(), "".join(map(str.rstrip,next(groups)[1],""))
            d[key] = val
f.close()


def revc(s):
	sc=""
	for base in range(len(s)):
		n = len(s) - base - 1
		if s[n] == "A":
			sc += "T"
		elif s[n] == "C":
			sc += "G"
		elif s[n] == "G":
			sc += "C"
		else:
			sc += "A"
	return sc



s = d.values()[0]

for i in range(4, 21):
	for j in range(len(s)):
		if i + j < len(s) + 1:
			if s[j:j+i] == revc(s[j:j+i]):
				print str(j+1) + " " + str(i)
