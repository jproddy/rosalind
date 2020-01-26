codon={											#s=STOP
"UUU":"F", "CUU": "L", "AUU":"I", "GUU": "V",
"UUC":"F", "CUC": "L", "AUC":"I", "GUC": "V",
"UUA":"L", "CUA": "L", "AUA":"I", "GUA": "V",
"UUG":"L", "CUG": "L", "AUG":"M", "GUG": "V",
"UCU":"S", "CCU": "P", "ACU":"T", "GCU": "A",
"UCC":"S", "CCC": "P", "ACC":"T", "GCC": "A",
"UCA":"S", "CCA": "P", "ACA":"T", "GCA": "A",
"UCG":"S", "CCG": "P", "ACG":"T", "GCG": "A",
"UAU":"Y", "CAU": "H", "AAU":"N", "GAU": "D",
"UAC":"Y", "CAC": "H", "AAC":"N", "GAC": "D",
"UAA":"s", "CAA": "Q", "AAA":"K", "GAA": "E",
"UAG":"s", "CAG": "Q", "AAG":"K", "GAG": "E",
"UGU":"C", "CGU": "R", "AGU":"S", "GGU": "G",
"UGC":"C", "CGC": "R", "AGC":"S", "GGC": "G",
"UGA":"s", "CGA": "R", "AGA":"R", "GGA": "G",
"UGG":"W", "CGG": "R", "AGG":"R", "GGG": "G"
}

from itertools import groupby
with open("rosalind_orf.txt") as f:
    groups = groupby(f, key=lambda x: not x.startswith(">"))
    d = {}
    for k,v in groups:
        if not k:
            key, val = list(v)[0].rstrip(), "".join(map(str.rstrip,next(groups)[1],""))
            d[key] = val
f.close()

def revc(s):		#reverse complement
	sc = ""
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

def torna(dna):
	rna = ""
	for base in range(len(dna)):
		if dna[base] == "T":
			rna += "U"
		else:
			rna += dna[base]
	return rna

s = d.values()[0]
t = revc(s)

prots = []
candidates = []
srna = torna(s)
trna = torna(t)

for j in range(0, 3):
	temp = srna[j:]
	prots.append("")
	for i in range(len(temp)/3):
		prots[j] += codon[temp[3*i:3*i+3]]
for j in range(0, 3):
	temp = trna[j:]
	prots.append("")
	for i in range(len(temp)/3):
		prots[j+3] += codon[temp[3*i:3*i+3]]

for i in range(len(prots)):
	for j in range(len(prots[i])):
		if prots[i][j] == "M":
			for k in range(j+1, len(prots[i])):
				if prots[i][k] == "s" and prots[i][j:k] not in candidates and "s" not in prots[i][j:k]: #something ugly af here
					candidates.append(prots[i][j:k])
					break

candidates.sort()
for i in candidates:
	print i
