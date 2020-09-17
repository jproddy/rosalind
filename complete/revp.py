'''
Locating Restriction Sites
http://rosalind.info/problems/revp/

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
'''
from utils.parse_fasta import parse_fasta_as_list
import revc

filename = 'rosalind_revp.txt'

def reverse_palindromes(dna):
	sites = []
	for length in range(4, 13):
		for start in range(0, len(dna) - length + 1):
			segment = dna[start:start+length]
			if segment == revc.reverse_complement(segment):
				sites.append((start+1, length))
	return sites

def main():
	with open(filename) as f:
		fasta = f.read()
	dna = parse_fasta_as_list(fasta)[0]
	print('\n'.join([' '.join(str(i) for i in site) for site in reverse_palindromes(dna)]))

if __name__ == '__main__':
	main()
