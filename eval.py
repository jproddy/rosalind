f = open("rosalind_eval.txt", "r")
lines = f.readlines()
f.close()

n = int(lines[0].strip())
s = lines[1].strip()
A = [float(x) for x in lines[2].strip().split(" ")]
B = []

gc_s = s.count("G") + s.count("C")

for i in range(len(A)):
	B.append((n-len(s)+1) * (A[i]/2)**gc_s * ((1-A[i])/2) ** (len(s)-gc_s))

print ' '.join(map(str, B))