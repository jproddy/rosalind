from itertools import groupby
with open("rosalind_splc.txt") as f:
    groups = groupby(f, key=lambda x: not x.startswith(">"))
    d = {}
    for k,v in groups:
        if not k:
            key, val = list(v)[0].rstrip(), "".join(map(str.rstrip,next(groups)[1],""))
            d[key] = val
f.close()

codon={
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
"UAA":"", "CAA": "Q", "AAA":"K", "GAA": "E",
"UAG":"", "CAG": "Q", "AAG":"K", "GAG": "E",
"UGU":"C", "CGU": "R", "AGU":"S", "GGU": "G",
"UGC":"C", "CGC": "R", "AGC":"S", "GGC": "G",
"UGA":"", "CGA": "R", "AGA":"R", "GGA": "G",
"UGG":"W", "CGG": "R", "AGG":"R", "GGG": "G"
}

exon = max(d.values(), key=len)
print exon
introns = d.values()
introns.remove(exon)


for i in introns:
	exon = exon.replace(i, "")


exonrna = ""
for base in range(len(exon)):
	if exon[base] == "T":
		exonrna += "U"
	else:
		exonrna += exon[base]	

exonprot = ""
for i in range(len(exonrna)/3):
	exonprot += codon[exonrna[3*i:3*i+3]]

print exonprot