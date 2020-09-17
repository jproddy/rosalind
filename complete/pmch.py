'''
Perfect Matchings and RNA Secondary Structures
http://rosalind.info/problems/pmch/

Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
'''
from math import factorial
from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_pmch.txt'

def perfect_matchings(rna):
	return factorial(rna.count('A')) * factorial(rna.count('C'))

def main():
	with open(filename) as f:
		fasta = f.read()
	rna = parse_fasta_as_list(fasta)[0]
	print(perfect_matchings(rna))

if __name__ == '__main__':
	main()
