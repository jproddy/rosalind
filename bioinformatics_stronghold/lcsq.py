'''
Finding a Shared Spliced Motif
http://rosalind.info/problems/lcsq/

Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.

Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)
'''
import numpy as np

from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_lcsq.txt'

def longest_common_subsequence(s1, s2):
	# copied from bioinformatics_textbook_track/ba5c
	# generate array with 1 extra row and col to simplify conditions in loop
	len1, len2 = len(s1), len(s2)
	arr = np.zeros((len1+1, len2+1), dtype=int)

	# solve for subsequences
	for i1 in range(len1-1, -1, -1):
		for i2 in range(len2-1, -1, -1):
			if s1[i1] == s2[i2]:
				arr[i1, i2] = 1 + arr[i1+1, i2+1]
			else:
				arr[i1, i2] = max(arr[i1+1, i2], arr[i1, i2+1])

	# (re?)build the solution
	seq = []
	i1, i2 = 0, 0
	while i1 < len1 and i2 < len2:
		if s1[i1] == s2[i2]:
			seq.append(s1[i1])
			i1 += 1
			i2 += 1
		elif arr[i1+1, i2] > arr[i1, i2+1]:
			i1 += 1
		else:
			i2 += 1

	return ''.join(seq)

def main():
	with open(filename) as f:
		s1, s2 = parse_fasta_as_list(f.read())
	print(longest_common_subsequence(s1, s2))

if __name__ == '__main__':
	main()
