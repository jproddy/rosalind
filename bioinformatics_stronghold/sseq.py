'''
Finding a Spliced Motif
http://rosalind.info/problems/sseq/

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
'''
from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_sseq.txt'

def spliced_indices(s, t):
	indices = []
	t_i, s_i = 0, 0
	while t_i < len(t):
		if t[t_i] == s[s_i]:
			indices.append(s_i + 1)
			t_i += 1
		s_i += 1
	return indices

def main():
	with open(filename) as f:
		fasta = f.read()
	s, t = parse_fasta_as_list(fasta)
	print(' '.join([str(i) for i in spliced_indices(s, t)]))

if __name__ == '__main__':
	main()
