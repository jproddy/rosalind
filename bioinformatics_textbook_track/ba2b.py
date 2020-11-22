'''
Find a Median String
http://rosalind.info/problems/ba2b/

Given: An integer k and a collection of strings Dna.

Return: A k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern. (If multiple answers exist, you may return any one.)
'''
from ba2h import distance_between_pattern_and_strings
from ba1i import lex_kmers

filename = 'rosalind_ba2b.txt'

def find_median_string(k, dnas):
	# brute force
	kmers = lex_kmers(['A', 'C', 'G', 'T'], k)
	min_d = float('inf')
	for kmer in kmers:
		d = distance_between_pattern_and_strings(kmer, dnas)
		if d < min_d:
			min_d = d
			min_kmer = kmer
	return min_kmer
	

def main():
	with open(filename) as f:
		k = int(f.readline().strip())
		dnas = [line.strip() for line in f.readlines()]
	print(find_median_string(k, dnas))

if __name__ == '__main__':
	main()
