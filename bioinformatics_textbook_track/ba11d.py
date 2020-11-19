'''
Convert a Peptide Vector into a Peptide
http://rosalind.info/problems/ba11d/

Given: A space-delimited binary vector P.

Return: A peptide whose binary peptide vector matches P. For masses with more than one amino acid, any choice may be used.
'''
from utils.monoisotopic_mass_table import int_immt

filename = 'rosalind_ba11d.txt'

def peptide_vector_to_peptide(P):
	masses = [0] + [i + 1 for i, val in enumerate(P) if val]
	amino_acids = [int_immt[j-i] for i, j in zip(masses, masses[1:])]
	return ''.join(amino_acids)

def main():
	with open(filename) as f:
		P = list(map(int, f.readline().strip().split()))
	print(peptide_vector_to_peptide(P))

if __name__ == '__main__':
	main()
