'''
Find a Highest-Scoring Local Alignment of Two Strings
http://rosalind.info/problems/ba5f/

Given: Two amino acid strings.

Return: The maximum score of a local alignment of the strings, followed by a local alignment of these strings achieving the maximum score. Use the PAM250 scoring matrix and indel penalty σ = 5. (If multiple local alignments achieving the maximum score exist, you may return any one.)
'''
import numpy as np

filename = 'rosalind_ba5f.txt'

def local_alignment(s1, s2, scoring_matrix='PAM250', indel_penalty=5):
	# https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm
	if scoring_matrix == 'PAM250':
		from utils.scoring_matrices import PAM250 as sm
	else:
		return

	# generate matrix
	matrix = np.zeros((len(s2) + 1, len(s1) + 1), dtype=int)

	# fill rest of matrix
	for r in range(1, len(s2) + 1):
		for c in range(1, len(s1) + 1):
			down = matrix[r-1, c] - indel_penalty
			right = matrix[r, c-1] - indel_penalty
			diag = matrix[r-1, c-1] + sm.loc[s1[c-1], s2[r-1]]
			matrix[r, c] = max(down, right, diag, 0)

	max_indices = np.where(matrix == matrix.max())

	# backtrack solution
	r, c = max_indices[0][0], max_indices[1][0]
	score = matrix[r, c]
	s1_aligned = []
	s2_aligned = []
	while r and c:
		if matrix[r, c] == 0:
			break
		elif matrix[r, c] == matrix[r-1, c] - indel_penalty: # go up
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
