'''
Creating a Character Table from Genetic Strings
http://rosalind.info/problems/cstr/

Given: A collection of at most 100 characterizable DNA strings, each of length at most 300 bp.

Return: A character table for which each nontrivial character encodes the symbol choice at a single position of the strings. (Note: the choice of assigning '1' and '0' to the two states of each SNP in the strings is arbitrary.)
'''
import numpy as np

filename = 'rosalind_cstr.txt'

def genetic_character_table(dnas):
	arr = np.array([list(dna) for dna in dnas])
	arr = (arr == arr[0]).astype(int)
	arr_s = arr.sum(axis=0)
	valid_cols = (len(arr) - 1 > arr_s) & (arr_s > 1)
	return [''.join(row) for row in arr[:, valid_cols].T.astype(str)]

def main():
	with open(filename) as f:
		dnas = [line.strip() for line in f.readlines()]
	print(*genetic_character_table(dnas), sep='\n')

if __name__ == '__main__':
	main()
