# the filename glob.py breaks numpy!
'''
Global Alignment with Scoring Matrix
http://rosalind.info/problems/glob/

The BLOSUM62 scoring matrix.
Linear gap penalty equal to 5 (i.e., a cost of -5 is assessed for each gap symbol).
'''
import numpy as np

from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_glob.txt'

def global_alignment(s1, s2, scoring_matrix='BLOSUM62', indel_penalty=5):
	# copied from bioinformatics_textbook_track/ba5e
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

	return matrix[-1, -1] 

def main():
	with open(filename) as f:
		s1, s2 = parse_fasta_as_list(f.read())
	print(global_alignment(s1, s2))

if __name__ == '__main__':
	main()
