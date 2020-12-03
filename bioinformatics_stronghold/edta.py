'''
Edit Distance Alignment
http://rosalind.info/problems/edta/

Given: Two protein strings s and t in FASTA format (with each string having length at most 1000 aa).

Return: The edit distance dE(s,t) followed by two augmented strings s′ and t′ representing an optimal alignment of s and t.
'''
import numpy as np

from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_edta.txt'

def global_alignment(s1, s2, mismatch_penalty=1, indel_penalty=1):
	# slight deviation from bioinformatics_textbook_track/ba5e
	# https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
	# generate matrix and preliminarily fill
	matrix = np.zeros((len(s2) + 1, len(s1) + 1), dtype=int)
	matrix[0, :] = np.arange(0, (len(s1)+1) * indel_penalty, indel_penalty)
	matrix[:, 0] = np.arange(0, (len(s2)+1) * indel_penalty, indel_penalty)

	# fill rest of matrix
	for r in range(1, len(s2) + 1):
		for c in range(1, len(s1) + 1):
			down = matrix[r-1, c] + indel_penalty
			right = matrix[r, c-1] + indel_penalty
			diag = matrix[r-1, c-1] + (s1[c-1] != s2[r-1])
			matrix[r, c] = min(down, right, diag)

	# backtrack solution
	r, c = len(s2), len(s1)
	s1_aligned = []
	s2_aligned = []
	while r and c:
		if matrix[r, c] == matrix[r-1, c] + indel_penalty: # go up
			s1_aligned.append('-')
			s2_aligned.append(s2[r-1])
			r -= 1
		elif matrix[r, c] == matrix[r, c-1] + indel_penalty: # go left
			s1_aligned.append(s1[c-1])
			s2_aligned.append('-')
			c -= 1
		else:
			s1_aligned.append(s1[c-1])
			s2_aligned.append(s2[r-1])
			r -= 1
			c -= 1
	if c:
		s1_aligned.extend(s1[:c])
		s2_aligned.extend(['-'] * c)
	elif r:
		s1_aligned.extend(['-'] * r)
		s2_aligned.extend(s2[:r])

	# score, aligned s1, aligned s2
	return matrix[-1, -1], ''.join(reversed(s1_aligned)), ''.join(reversed(s2_aligned))

def main():
	with open(filename) as f:
		s1, s2 = parse_fasta_as_list(f.read())
	print(*global_alignment(s1, s2), sep='\n')

if __name__ == '__main__':
	main()
