'''
Global Alignment with Constant Gap Penalty
http://rosalind.info/problems/gcon/

Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).

Return: The maximum alignment score between s and t. Use:

The BLOSUM62 scoring matrix.
Constant gap penalty equal to 5.
'''
import numpy as np

from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_gcon.txt'

def global_alignment_constant_gap(s, t, scoring_matrix='BLOSUM62', gap_penalty=5):
	if scoring_matrix == 'BLOSUM62':
		from utils.scoring_matrices import BLOSUM62 as sm
	else:
		return

	# matrix with overall best alignment
	matrix = np.zeros((len(t) + 1, len(s) + 1), dtype=int)
	matrix[0, 1:] = -gap_penalty
	matrix[1:, 0] = -gap_penalty

	# matrix assuming last pair matches s_i, t_j
	matrix_st = np.zeros((len(t) + 1, len(s) + 1), dtype=int)
	# matrix assuming last pair matches s_i with space
	matrix_t_ = np.zeros((len(t) + 1, len(s) + 1), dtype=int)
	matrix_t_[0, :] = -999999 # ideally -inf, but can overflow with dtype=int
	# matrix assuming last pair matches space with t_j
	matrix__s = np.zeros((len(t) + 1, len(s) + 1), dtype=int)
	matrix__s[:, 0] = -999999 # ideally -inf, but can overflow with dtype=int

	for r in range(1, len(t) + 1):
		for c in range(1, len(s) + 1):
			matrix_st[r, c] = matrix[r-1, c-1] + sm.loc[t[r-1], s[c-1]]
			matrix_t_[r, c] = max(matrix[r-1, c] - gap_penalty, matrix_t_[r-1, c])
			matrix__s[r, c] = max(matrix[r, c-1] - gap_penalty, matrix__s[r, c-1])

			matrix[r,c] = max(matrix_st[r, c], matrix_t_[r, c], matrix__s[r,c])

	return matrix[-1, -1]

def main():
	with open(filename) as f:
		s, t = parse_fasta_as_list(f.read())
	print(global_alignment_constant_gap(s, t))

if __name__ == '__main__':
	main()
