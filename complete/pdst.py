'''
Creating a Distance Matrix
http://rosalind.info/problems/pdst/

Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is allowed an absolute error of 0.001.
'''
import numpy as np
from utils.parse_fasta import parse_fasta_as_list
from hamm import hamming_distance

filename = 'rosalind_pdst.txt'

def distance_matrix(dnas):
	l = len(dnas[0])
	n = len(dnas)
	matrix = np.zeros((n, n))
	for r in range(n):
		for c in range(r+1, n):
			matrix[r, c] = hamming_distance(dnas[r], dnas[c]) / l
	matrix += matrix.T
	return matrix

def main():
	with open(filename) as f:
		fasta = f.read()
	dnas = parse_fasta_as_list(fasta)
	print('\n'.join([' '.join([str(col) for col in row]) for row in distance_matrix(dnas)]))

if __name__ == '__main__':
	main()
