'''
Inferring Genotype from a Pedigree
http://rosalind.info/problems/mend/

Given: A rooted binary tree T in Newick format encoding an individual's pedigree for a Mendelian factor whose alleles are A (dominant) and a (recessive).

Return: Three numbers between 0 and 1, corresponding to the respective probabilities that the individual at the root of T will exhibit the "AA", "Aa" and "aa" genotypes.
'''
from utils.newick import NewickParser

filename = 'rosalind_mend.txt'

def get_genotype(node):
	if node.name == 'AA':
		return (1, 0, 0)
	elif node.name == 'Aa':
		return (0, 1, 0)
	elif node.name == 'aa':
		return (0, 0, 1)
	
	c0 = get_genotype(node.children[0])
	c1 = get_genotype(node.children[1])

	c0_A = ((2 * c0[0]) + c0[1]) / 2
	c0_a = (c0[1] + (2 * c0[2])) / 2
	c1_A = ((2 * c1[0]) + c1[1]) / 2
	c1_a = (c1[1] + (2 * c1[2])) / 2

	AA = (c0_A * c1_A)
	Aa = ((c0_A * c1_a) + (c0_a * c1_A))
	aa = (c0_a * c1_a)

	return AA, Aa, aa

def main():
	with open(filename) as f:
		line = f.readline().strip()
	parser = NewickParser()
	tree = parser.parse(line)
	print(*get_genotype(tree))

if __name__ == '__main__':
	main()
