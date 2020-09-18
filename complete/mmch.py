'''
Maximum Matchings and RNA Secondary Structures
http://rosalind.info/problems/mmch/

Given: An RNA string s of length at most 100.

Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s
'''
from collections import Counter
from utils.parse_fasta import parse_fasta_as_list
from pper import partial_permutations

filename = 'rosalind_mmch.txt'

def max_matchings(rna):
	count = Counter(rna)
	return partial_permutations(max(count['A'], count['U']), min(count['A'], count['U'])) * \
				partial_permutations(max(count['C'], count['G']), min(count['C'], count['G']))

def main():
	with open(filename) as f:
		fasta = f.read()
	rna = parse_fasta_as_list(fasta)[0]
	print(max_matchings(rna))

if __name__ == '__main__':
	main()
