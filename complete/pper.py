f = open("rosalind_pper.txt", "r")
s = f.read()
f.close()

slist = [int(x) for x in s.split(" ")]

t = slist[0] #total
s = slist[1] #subset

pper = 1

for i in range(t-s+1, t+1):
	pper *= i
	pper = pper % 1000000

print pper