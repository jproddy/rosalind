'''
Overlap Alignment
http://rosalind.info/problems/oap/

Given: Two DNA strings s and t in FASTA format, each having length at most 10 kbp.

Return: The score of an optimal overlap alignment of s and t, followed by an alignment of a suffix s′ of s and a prefix t′ of t achieving this optimal score. Use an alignment score in which matching symbols count +1, substitutions count -2, and there is a linear gap penalty of 2. If multiple optimal alignments exist, then you may return any one.
'''
import numpy as np

from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_oap.txt'

def local_alignment(s1, s2, match_score=1, mismatch_penalty=2, indel_penalty=2):
	# copied from bioinformatics_textbook_track/ba5i
	# https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm
	# generate matrix
	matrix = np.zeros((len(s2) + 1, len(s1) + 1), dtype=int)
	matrix[:, 0] = np.arange(0, -(len(s2) + 1) * indel_penalty, -indel_penalty)

	# fill rest of matrix
	for r in range(1, len(s2) + 1):
		print(r)
		for c in range(1, len(s1) + 1):
			down = matrix[r-1, c] - indel_penalty
			right = matrix[r, c-1] - indel_penalty
			diag = match_score if s1[c-1] == s2[r-1] else -mismatch_penalty
			diag += matrix[r-1, c-1]
			matrix[r, c] = max(down, right, diag)

	# backtrack solution--argmax here ensures that we find the shortest overlap
	# with the max score
	r, c = matrix[:, -1].argmax(), len(s1)
	score = matrix[r, c]
	s1_aligned = []
	s2_aligned = []
	while r:
		if matrix[r, c] == matrix[r-1, c] - indel_penalty: # go up
			s1_aligned.append('-')
			s2_aligned.append(s2[r-1])
			r -= 1
		elif matrix[r, c] == matrix[r, c-1] - indel_penalty: # go left
			s1_aligned.append(s1[c-1])
			s2_aligned.append('-')
			c -= 1
		else:
			s1_aligned.append(s1[c-1])
			s2_aligned.append(s2[r-1])
			r -= 1
			c -= 1

	return score, ''.join(reversed(s1_aligned)), ''.join(reversed(s2_aligned))

def main():
	with open(filename) as f:
		s1, s2 = parse_fasta_as_list(f.read())
		print(len(s1), len(s2))

	print(*local_alignment(s1, s2), sep='\n')

if __name__ == '__main__':
	main()
