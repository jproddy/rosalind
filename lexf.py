from itertools import permutations

f = open("rosalind_lexf.txt", "r")
s = f.readlines()
f.close()

oa = s[0].strip().split(" ") # ordered alphabet
d = int(s[1].strip()) # depth
a = oa * d # "full" alphabet

perm=permutations(a,d)
p=list(perm)
p.sort()
q=[]

for i in p:
	if i not in q:
		q.append(i)


for i in range(len(q)):
	print ''.join(map(str, q[i]))