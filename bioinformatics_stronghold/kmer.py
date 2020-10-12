'''
k-Mer Composition
http://rosalind.info/problems/kmer/

Given: A DNA string s in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s.
'''
from utils.parse_fasta import parse_fasta_as_list
from lexf import lex_kmers

filename = 'rosalind_kmer.txt'

def kmer_composition(dna, alphabet=['A','C','G','T'], k=4):
	kmers = lex_kmers(alphabet, k)
	kmer_dict = {}
	for i in range(len(dna) - k + 1):
		s = dna[i:i+k]
		kmer_dict[s] = kmer_dict.get(s, 0) + 1
	return [kmer_dict.get(kmer, 0) for kmer in kmers]

def main():
	with open(filename) as f:
		fasta = f.read()
	dna = parse_fasta_as_list(fasta)[0]
	print(' '.join([str(i) for i in kmer_composition(dna)]))

if __name__ == '__main__':
	main()
