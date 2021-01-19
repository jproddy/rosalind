'''
Global Alignment with Scoring Matrix and Affine Gap Penalty
http://rosalind.info/problems/gaff/

Given: Two protein strings s and t in FASTA format (each of length at most 100 aa).

Return: The maximum alignment score between s and t, followed by two augmented strings s′ and t′ representing an optimal alignment of s and t. Use:

The BLOSUM62 scoring matrix.
Gap opening penalty equal to 11.
Gap extension penalty equal to 1.
'''
import numpy as np

from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_gaff.txt'

def global_alignment_constant_gap(s, t, scoring_matrix='BLOSUM62', gap_open_penalty=11, gap_exten_penalty=1):
	# slight derivative of gcon, then add backtracking
	if scoring_matrix == 'BLOSUM62':
		from utils.scoring_matrices import BLOSUM62 as sm
	else:
		return

	# matrix with overall best alignment
	matrix = np.zeros((len(t) + 1, len(s) + 1), dtype=int)
	matrix[0, 1:] = np.arange(-gap_open_penalty, -(len(s) * gap_exten_penalty) - gap_open_penalty, -gap_exten_penalty)
	matrix[1:, 0] = np.arange(-gap_open_penalty, -(len(t) * gap_exten_penalty) - gap_open_penalty, -gap_exten_penalty)

	# matrix assuming last pair matches s_i, t_j
	matrix_ts = np.zeros((len(t) + 1, len(s) + 1), dtype=int)
	# matrix assuming last pair matches s_i with space
	matrix_t_ = np.zeros((len(t) + 1, len(s) + 1), dtype=int)
	matrix_t_[0, :] = -99999 # ideally -inf, but can overflow with dtype=int
	# matrix assuming last pair matches space with t_j
	matrix__s = np.zeros((len(t) + 1, len(s) + 1), dtype=int)
	matrix__s[:, 0] = -99999 # ideally -inf, but can overflow with dtype=int

	for r in range(1, len(t) + 1):
		for c in range(1, len(s) + 1):
			matrix_ts[r, c] = matrix[r-1, c-1] + sm.loc[t[r-1], s[c-1]]
			matrix_t_[r, c] = max(matrix[r-1, c] - gap_open_penalty, matrix_t_[r-1, c] - gap_exten_penalty)
			matrix__s[r, c] = max(matrix[r, c-1] - gap_open_penalty, matrix__s[r, c-1] - gap_exten_penalty)

			matrix[r,c] = max(matrix_ts[r, c], matrix_t_[r, c], matrix__s[r,c])

	# backtrack
	r, c = len(t), len(s)
	t_aligned, s_aligned = [], []
	while r and c:
		if matrix[r, c] == matrix__s[r, c]:
			t_aligned.append('-')
			s_aligned.append(s[c-1])
			c -= 1
		elif matrix[r, c] == matrix_t_[r, c]:
			t_aligned.append(t[r-1])
			s_aligned.append('-')
			r -= 1
		elif matrix[r, c] == matrix_ts[r, c]:
			t_aligned.append(t[r-1])
			s_aligned.append(s[c-1])
			r -= 1
			c -= 1

	# deal with residual 
	while r:
			t_aligned.append(t[r-1])
			s_aligned.append('-')
			r -= 1
	while c:
			t_aligned.append('-')
			s_aligned.append(s[c-1])
			c -= 1

	return matrix[-1, -1], ''.join(reversed(s_aligned)), ''.join(reversed(t_aligned))


def main():
	with open(filename) as f:
		s, t = parse_fasta_as_list(f.read())
	print(*global_alignment_constant_gap(s, t), sep='\n')

if __name__ == '__main__':
	main()
