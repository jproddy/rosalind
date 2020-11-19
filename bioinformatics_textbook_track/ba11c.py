'''
Convert a Peptide into a Peptide Vector
http://rosalind.info/problems/ba11c/

Given: A peptide P.

Return: The peptide vector of P.
'''
from utils.monoisotopic_mass_table import int_mmt

filename = 'rosalind_ba11c.txt'

def peptide_vector(P):
	vector = []
	for aa in P:
		vector.extend(([0] * (int_mmt[aa] - 1)) + [1])
	return vector

def main():
	with open(filename) as f:
		P = f.readline().strip()
	print(*peptide_vector(P))

if __name__ == '__main__':
	main()
