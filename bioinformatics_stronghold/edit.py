'''
Edit Distance
http://rosalind.info/problems/edit/

Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).

Return: The edit distance dE(s,t).
'''
import numpy as np

from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_edit.txt'

def edit_distance(s1, s2):
	# copied from bioinformatics_textbook_track/ba5g
	matrix = np.zeros((len(s2) + 1, len(s1) + 1), dtype=int)
	matrix[0, :] = np.arange(len(s1) + 1)
	matrix[:, 0] = np.arange(len(s2) + 1)

	for r in range(1, len(s2) + 1):
		for c in range(1, len(s1) + 1):
			if s1[c-1] == s2[r-1]:
				matrix[r, c] = matrix[r-1, c-1]
			else:
				matrix[r, c] = min(matrix[r, c-1], matrix[r-1, c], matrix[r-1, c-1]) + 1

	return(matrix[-1, -1])

def main():
	with open(filename) as f:
		s1, s2 = parse_fasta_as_list(f.read())
	print(edit_distance(s1, s2))

if __name__ == '__main__':
	main()
