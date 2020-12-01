'''
Compute the Edit Distance Between Two Strings
http://rosalind.info/problems/ba5g/

Given: Two amino acid strings.

Return: The edit distance between these strings.
'''
import numpy as np

filename = 'rosalind_ba5g.txt'

def edit_distance(s1, s2):
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
		s1 = f.readline().strip()
		s2 = f.readline().strip()
	print(edit_distance(s1, s2))

if __name__ == '__main__':
	main()
