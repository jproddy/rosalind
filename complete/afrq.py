import math

f = open("rosalind_afrq.txt", "r")
s = f.read()
f.close()


A=[float(i) for i in s.strip().split(" ")]

rec = []
dom = []
atleastonerec = []

for i in A:
	rec.append(math.sqrt(i))
for i in rec:
	dom.append(1 - i)
for i in range(len(A)):
	atleastonerec.append(rec[i]**2 + 2*rec[i]*dom[i])

print ' '.join(map(str, atleastonerec))