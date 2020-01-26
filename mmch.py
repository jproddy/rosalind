f = open("rosalind_mmch.txt", "r")
s = f.read()
f.close()

a = s.count("A")
c = s.count("C")
g = s.count("G")
u = s.count("U")

mm=1

for i in range(max([a,u])-min([a,u])+1, max([a,u])+1):
	# print mm
	mm*=i

for i in range(max([c,g])-min([c,g])+1, max([c,g])+1):
	# print mm
	mm*=i

print mm