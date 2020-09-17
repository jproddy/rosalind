'''
Translating RNA into Protein
http://rosalind.info/problems/prot/

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
'''
from utils.codon_table import codons, codons_star_stop

filename = 'rosalind_prot.txt'

def translate(rna, stop=None):
	if stop == '*':
		return ''.join([codons_star_stop[rna[3*i : 3*i+3]] for i in range(len(rna) // 3)])
	return ''.join([codons[rna[3*i : 3*i+3]] for i in range(len(rna) // 3)])

def main():
	with open(filename) as f:
		rna = f.readline().strip()
	# exclude terminal STOP codon
	print(translate(rna)[:-4])

if __name__ == '__main__':
	main()
