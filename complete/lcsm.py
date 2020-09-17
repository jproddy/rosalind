'''
Finding a Shared Motif
http://rosalind.info/problems/lcsm/

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
'''
from utils.parse_fasta import parse_fasta_as_list
filename = 'rosalind_lcsm.txt'


def longest_common_substring(dnas):
	# brute force with pretty poor runtime--O(dna_length^2 * number_of_dnas)
	# there are undoubtedly more efficient solutions
	lcs = ''
	# if working with strands of varied lengths, would likely be more efficient to find
	# the shortest string to use as the base, but all strings given are exactly 1 kpb
	l = len(dnas[0])
	for start in range(l):
		for end in range(l, start, -1):
			if end - start <= len(lcs):
				break
			elif all(dnas[0][start:end] in dna for dna in dnas[1:]):
				lcs = dnas[0][start:end]
	return lcs

def main():
	with open(filename) as f:
		fasta = f.read()
	dnas = parse_fasta_as_list(fasta)
	print(longest_common_substring(dnas))

if __name__ == '__main__':
	main()
