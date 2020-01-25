f = open("rosalind_iev.txt", "r")
s = f.read()
f.close()

num = [int(x) for x in s.split(" ")]

#num=[19310, 17533, 18385, 19004, 16736, 19151]
rat = [1, 1, 1, .75, .5, 0]
exp = []

for i in range(6):
	exp.append(2*num[i]*rat[i])

print sum(exp)