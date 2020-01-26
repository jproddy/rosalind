f = open("rosalind_sexl.txt", "r")
s = f.read()
f.close()

A = [float(i) for i in s.strip().split()]
B = []
for i in A:
	B.append(2 * i * (1-i))

print ' '.join(map(str, B))