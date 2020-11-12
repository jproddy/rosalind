"""
Find Frequent Words with Mismatches and Reverse Complements
http://rosalind.info/problems/ba1j/

Given: A DNA string Text as well as integers k and d.

Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible k-mers.
"""
from collections import Counter

from ba1c import reverse_complement
from ba1h import sc_hamming_distance
from ba1i import lex_kmers

filename = "rosalind_ba1j.txt"

def kmers_mismatches_revc(text, k, d):
	text_revc = reverse_complement(text)
	c = Counter(
		[text[i : i + k] for i in range(len(text) - k + 1)]
		+ [text_revc[i : i + k] for i in range(len(text_revc) - k + 1)]
	)
	mismatches = {kmer: c.get(kmer, 0) for kmer in lex_kmers(["A", "C", "G", "T"], k)}
	kmers = list(mismatches.keys())
	max_freq = 0
	for i in range(len(kmers) - 1):
		for j in range(i + 1, len(kmers)):
			if sc_hamming_distance(kmers[i], kmers[j], d):
				mismatches[kmers[i]] += c[kmers[j]]
				mismatches[kmers[j]] += c[kmers[i]]
				max_freq = max(max_freq, mismatches[kmers[i]], mismatches[kmers[j]])

	return [k for k, v in mismatches.items() if v == max_freq]

def main():
	with open(filename) as f:
		text = f.readline().strip()
		k, d = list(map(int, f.readline().strip().split()))
	print(*kmers_mismatches_revc(text, k, d))

if __name__ == "__main__":
	main()
