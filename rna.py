f = open("rosalind_rna.txt", "r")
dna = f.read()
f.close()

rna = ""

for base in range(len(dna)):
	if dna[base] == "T":
		rna += "U"
	else:
		rna += dna[base]

print rna