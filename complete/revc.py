f = open("rosalind_revc.txt", "r")
s = f.read()
f.close()

sc = ""

for base in range(len(s):
	n = ls-base-1
	if s[n] == "A":
		sc += "T"
	elif s[n] == "C":
		sc += "G"
	elif s[n] == "G":
		sc += "C"
	else:
		sc += "A"

print sc