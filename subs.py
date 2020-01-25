f = open("rosalind_subs.txt", "r")
s = f.read()
f.close()

slist = s.split("\n")

s = slist[0]
t = slist[1]

loc=[]

for i in range(len(s) - len(t)):
	if s[i:i+len(t)] == t:
		loc.append(str(i+1))


print " ".join(loc)