'''
Find Patterns Forming Clumps in a String
http://rosalind.info/problems/ba1e/

Given: A string Genome, and integers k, L, and t.

Return: All distinct k-mers forming (L, t)-clumps in Genome.
'''
from collections import Counter

from ba1d import pattern_indices

filename = 'rosalind_ba1e.txt'

def clumps(genome, k, L, t):
	c = Counter([genome[i:i+k] for i in range(len(genome)-k+1)])
	test_patterns = [pattern for pattern in c if c[pattern] >= t]
	kmer_clumps = []
	for pattern in test_patterns:
		indices = pattern_indices(pattern, genome)
		for i in range(len(indices) - t + 1):
			if indices[i+t-1] - indices[i] <= L - t + 1:
				kmer_clumps.append(pattern)
				break
	return kmer_clumps


	pass

def main():
	with open(filename) as f:
		genome = f.readline().strip()
		k, L, t = map(int, f.readline().strip().split())
	print(*clumps(genome, k, L, t))

if __name__ == '__main__':
	main()
