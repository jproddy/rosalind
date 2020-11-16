'''
Translate an RNA String into an Amino Acid String
http://rosalind.info/problems/ba4a/

Given: An RNA string Pattern.

Return: The translation of Pattern into an amino acid string Peptide.
'''
from utils.codon_table import codons

filename = 'rosalind_ba4a.txt'

def translate(pattern):
	return ''.join([codons[pattern[3*i:3*i+3]] for i in range(len(pattern) // 3)][:-1])

def main():
	with open(filename) as f:
		pattern = f.readline()
	print(translate(pattern))

if __name__ == '__main__':
	main()
