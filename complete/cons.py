'''
Consensus and Profile
http://rosalind.info/problems/cons/

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
'''
import numpy as np
from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_cons.txt'

def consensus_and_profile(dnas):
	arr = np.array([list(dna) for dna in dnas])
	a = (arr == 'A').sum(axis=0)
	c = (arr == 'C').sum(axis=0)
	g = (arr == 'G').sum(axis=0)
	t = (arr == 'T').sum(axis=0)
	maxes = np.array([a, c, g, t]).max(axis=0)
	consensus = np.where(a == maxes, 'A', \
					np.where(c == maxes, 'C', \
					np.where(g == maxes, 'G', 'T')))
	return a, c, g, t, consensus

def main():
	with open(filename) as f:
		fasta = f.read()
	dnas = parse_fasta_as_list(fasta)
	a, c, g, t, consensus = consensus_and_profile(dnas)
	print(''.join(consensus))
	print('A:', ' '.join([str(i) for i in a]))
	print('C:', ' '.join([str(i) for i in c]))
	print('G:', ' '.join([str(i) for i in g]))
	print('T:', ' '.join([str(i) for i in t]))


if __name__ == '__main__':
	main()
