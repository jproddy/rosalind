'''
Translating RNA into Protein
http://rosalind.info/problems/prot/

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
'''
from utils.codon_table import codons

filename = 'rosalind_prot.txt'

def translate(rna):
	# exclude terminal STOP codon
	return ''.join([codons[rna[3*i : 3*i+3]] for i in range(len(rna) // 3)][:-1])

def main():
	with open(filename) as f:
		rna = f.readline().strip()
	print(translate(rna))

if __name__ == '__main__':
	main()
