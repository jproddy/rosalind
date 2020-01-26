f = open("rosalind_sset.txt", "r")
s = f.read()
f.close()

n = int(s.strip())

sset = 1

for i in range(n):
	sset *= 2
	sset = sset % 1000000

print sset