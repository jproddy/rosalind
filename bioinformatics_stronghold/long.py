'''
Genome Assembly as Shortest Superstring
http://rosalind.info/problems/long/

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
'''
from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_long.txt'

def align_strands(dnas):
	dna = dnas[0]
	strands = dnas[1:]
	while strands:
		for i, s in enumerate(strands):
			break_loop = False
			for j in range(len(s)//2):
				# append new string
				if s[:len(s)-j] ==  dna[-len(s)+j:]:
					dna = dna + s[len(s)-j:]
					break_loop = True
				# prepend new string
				elif s[j:] == dna[:len(s)-j]:
					dna = s[:j] + dna
					break_loop = True
				if break_loop:
					break
			if break_loop:
				strands.pop(i)
				break
	return dna

def main():
	with open(filename) as f:
		fasta = f.read()
	dnas = parse_fasta_as_list(fasta)
	print(align_strands(dnas))

if __name__ == '__main__':
	main()
