f = open("rosalind_pmch.txt", "r")
s = f.read()
f.close()

a = s.count("A")
c = s.count("C")

perf = 1

for i in range(1, a+1):
	perf *= i
for i in range(1, c+1):
	perf *= i

print perf