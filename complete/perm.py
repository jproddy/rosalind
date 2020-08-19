from itertools import permutations

f = open("rosalind_perm.txt", "r")
s = f.read()
f.close()

num = [int(x) for x in s.split(" ")]

perm = permutations(range(1, num[0]+1))
p = list(perm)

print len(p)

for i in range(len(p)):
	print ' '.join(map(str, p[i]))