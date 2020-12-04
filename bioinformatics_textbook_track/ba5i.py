'''
Find a Highest-Scoring Overlap Alignment of Two Strings
http://rosalind.info/problems/ba5i/

Given: Two protein strings v and w, each of length at most 1000.

Return: The score of an optimal overlap alignment of v and w, followed by an alignment of a suffix v’ of v and a prefix w’ of w achieving this maximum score. Use an alignment score in which matches count +1 and both the mismatch and indel penalties are 2. (If multiple overlap alignments achieving the maximum score exist, you may return any one.)
'''
import numpy as np

filename = 'rosalind_ba5i.txt'

def local_alignment(s1, s2, match_score=1, mismatch_penalty=2, indel_penalty=2):
	# moderate deviation from ba5f
	# https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm
	# generate matrix
	matrix = np.zeros((len(s2) + 1, len(s1) + 1), dtype=int)
	matrix[:, 0] = np.arange(0, -(len(s2) + 1) * indel_penalty, -indel_penalty)

	# fill rest of matrix
	for r in range(1, len(s2) + 1):
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
		s1 = f.readline().strip()
		s2 = f.readline().strip()
	print(*local_alignment(s1, s2), sep='\n')

if __name__ == '__main__':
	main()
