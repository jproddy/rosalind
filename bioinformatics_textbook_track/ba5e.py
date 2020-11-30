'''
Find a Highest-Scoring Alignment of Two Strings
http://rosalind.info/problems/ba5e/

Given: Two amino acid strings.

Return: The maximum alignment score of these strings followed by an alignment achieving this maximum score. Use the BLOSUM62 scoring matrix and indel penalty σ = 5. (If multiple alignments achieving the maximum score exist, you may return any one.)
'''
import numpy as np

filename = 'rosalind_ba5e.txt'

def global_alignment(s1, s2, scoring_matrix='BLOSUM62', indel_penalty=5):
	# https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
	if scoring_matrix == 'BLOSUM62':
		from utils.scoring_matrices import BLOSUM62 as sm
	else:
		return

	# generate matrix and preliminarily fill
	matrix = np.zeros((len(s2) + 1, len(s1) + 1), dtype=int)
	matrix[0, :] = np.arange(0, -(len(s1)+1) * indel_penalty, -indel_penalty)
	matrix[:, 0] = np.arange(0, -(len(s2)+1) * indel_penalty, -indel_penalty)

	# fill rest of matrix
	for r in range(1, len(s2) + 1):
		for c in range(1, len(s1) + 1):
			down = matrix[r-1, c] - indel_penalty
			right = matrix[r, c-1] - indel_penalty
			diag = matrix[r-1, c-1] + sm.loc[s1[c-1], s2[r-1]]
			matrix[r, c] = max(down, right, diag)

	# backtrack solution
	r, c = len(s2), len(s1)
	s1_aligned = []
	s2_aligned = []
	while r and c:
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
		s1 = f.readline().strip()
		s2 = f.readline().strip()
	print(*global_alignment(s1, s2), sep='\n')

if __name__ == '__main__':
	main()
