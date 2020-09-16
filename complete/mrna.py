'''
Inferring mRNA from Protein
http://rosalind.info/problems/mrna/

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
'''
from collections import Counter
from utils.codon_table import codons

filename = 'rosalind_mrna.txt'

def n_valid_rna(protein):
	codon_counter = Counter(codons.values())
	n_valid = 3 # 3 Stop codons
	for aa in protein:
		n_valid *= codon_counter[aa]
	return n_valid

def main():
	with open(filename) as f:
		protein = f.readline().strip()
	print(n_valid_rna(protein) % 1000000)

if __name__ == '__main__':
	main()
