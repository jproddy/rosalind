'''
Generate the Frequency Array of a String
http://rosalind.info/problems/ba1k/

Given: A DNA string Text and an integer k.

Return: The frequency array of k-mers in Text.
'''
from collections import Counter

from ba1i import lex_kmers

filename = 'rosalind_ba1k.txt'

def freq_array(text, k):
	c = Counter([text[i : i + k] for i in range(len(text) - k + 1)])
	kmers = lex_kmers(['A', 'C', 'G', 'T'], k)
	return [c.get(kmer, 0) for kmer in kmers]

def main():
	with open(filename) as f:
		text = f.readline().strip()
		k = int(f.readline().strip())
	print(*freq_array(text, k))

if __name__ == '__main__':
	main()
