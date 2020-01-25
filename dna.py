f = open("rosalind_dna.txt", "r")
dna = f.read()
f.close()

a = str(dna.count("A"))
c = str(dna.count("C"))
g = str(dna.count("G"))
t = str(dna.count("T"))

print(a + " " + c + " " + g + " " + t)