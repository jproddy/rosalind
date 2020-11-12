'''
Find the Most Frequent Words with Mismatches in a String
http://rosalind.info/problems/ba1i/

Given: A string Text as well as integers k and d.

Return: All most frequent k-mers with up to d mismatches in Text.
'''
from collections import Counter

from ba1h import sc_hamming_distance

filename = 'rosalind_ba1i.txt'

def kmers_with_mismatches(text, k, d):
	c = Counter([text[i:i+k] for i in range(len(text)-k+1)])
	mismatches = {kmer: c.get(kmer, 0) for kmer in lex_kmers(['A', 'C', 'G', 'T'], k)}
	kmers = list(mismatches.keys())
	max_freq = 0
	for i in range(len(kmers) - 1):
		for j in range(i + 1, len(kmers)):
			if sc_hamming_distance(kmers[i], kmers[j], d):
				mismatches[kmers[i]] += c[kmers[j]]
				mismatches[kmers[j]] += c[kmers[i]]
				max_freq = max(max_freq, mismatches[kmers[i]], mismatches[kmers[j]])

	return [k for k, v in mismatches.items() if v == max_freq]

# generate all kmers--copied from bioinformatics_stronghold/lexf
def lex_kmers(alphabet, n):
	strings = []

	def helper(curr):
		if len(curr) == n:
			strings.append(curr)
		else:
			for char in alphabet:
				helper(curr + char)

	helper('')		
	return strings

def main():
	with open(filename) as f:
		text = f.readline().strip()
		k, d = list(map(int, f.readline().strip().split()))
	print(*kmers_with_mismatches(text, k, d))

if __name__ == '__main__':
	main()
