'''
Finding a Motif with Modifications
http://rosalind.info/problems/sims/

Given: Two DNA strings s and t, where s has length at most 10 kbp and t represents a motif of length at most 1 kbp.

Return: An optimal fitting alignment score with respect to the mismatch score defined above, followed by an optimal fitting alignment of a substring of s against t. If multiple such alignments exist, then you may output any one.
'''
import numpy as np

from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_sims.txt'

def fitting_alignment(v, w, match_score=1, mismatch_penalty=1, indel_penalty=1):
	# copied from bioinformatics_textbook_track/ba5h
	# assume len(v) >= len(w)
	# set up matrix with no penalty no matter where you start on longer string
	matrix = np.zeros((len(w) + 1, len(v) + 1), dtype=int)
	matrix[:, 0] = np.arange(0, -(len(w) + 1) * indel_penalty, -indel_penalty)

	# fill matrix
	for r in range(1, len(w) + 1):
		for c in range(1, len(v) + 1):
			if w[r-1] == v[c-1]:
				matrix[r, c] = matrix[r-1, c-1] + match_score
			else:
				matrix[r, c] =  max(
					matrix[r-1, c] - indel_penalty,
					matrix[r, c-1] - indel_penalty,
					matrix[r-1, c-1] - mismatch_penalty
				)

	# backtrack
	score = matrix[-1, :].max()
	r = len(w)
	c = matrix[-1, :].argmax()
	v_aligned, w_aligned = [], []
	while r:
		if w[r-1] == v[c-1] or matrix[r, c] == matrix[r-1, c-1] - mismatch_penalty:
			v_aligned.append(v[c-1])
			w_aligned.append(w[r-1])
			r -= 1
			c -= 1
		elif matrix[r, c] == matrix[r-1, c] - indel_penalty:
			v_aligned.append('-')
			w_aligned.append(w[r-1])
			r -= 1
		else:
			v_aligned.append(v[c-1])
			w_aligned.append('-')
			c -= 1

	return score, ''.join(reversed(v_aligned)), ''.join(reversed(w_aligned))

def main():
	with open(filename) as f:
		v, w = parse_fasta_as_list(f.read())
	print(*fitting_alignment(v, w), sep='\n')

if __name__ == '__main__':
	main()
