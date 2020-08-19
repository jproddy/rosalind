import math

f = open("rosalind_prob.txt", "r")
lines = f.readlines()
f.close()

s = lines[0].strip() # dna string
A = [float(x) for x in lines[1].strip().split(" ")] # GC content array

cg = s.count("C") + s.count("G")
at = s.count("A") + s.count("T")

B = [] # return prob

for i in range(len(A)):
	B.append(math.log10((A[i]/2)**cg * ((1-A[i])/2)**at))

s = ""

for i in range(len(B)):
	s += str(B[i]) + " "

print s
