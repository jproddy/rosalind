'''
Local Alignment with Scoring Matrix
http://rosalind.info/problems/loca/

Given: Two protein strings s and t in FASTA format (each having length at most 1000 aa).

Return: A maximum alignment score along with substrings r and u of s and t, respectively, which produce this maximum alignment score (multiple solutions may exist, in which case you may output any one).
Use:
The PAM250 scoring matrix.
Linear gap penalty equal to 5
'''
import numpy as np

from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_loca.txt'

def local_alignment(s1, s2, scoring_matrix='PAM250', indel_penalty=5):
	# copied with minor modification from bioinformatics_textbook_track/ba5f
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
			s2_aligned.append(s2[r-1])
			r -= 1
		elif matrix[r, c] == matrix[r, c-1] - indel_penalty: # go left
			s1_aligned.append(s1[c-1])
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
	print(*local_alignment(s1, s2), sep='\n')

if __name__ == '__main__':
	main()
