'''
Find the Length of a Longest Path in a Manhattan-like Grid
http://rosalind.info/problems/ba5b/

Given: Integers n and m, followed by an n × (m+1) matrix Down and an (n+1) × m matrix Right. The two matrices are separated by the "-" symbol.

Return: The length of a longest path from source (0, 0) to sink (n, m) in the n × m rectangular grid whose edges are defined by the matrices Down and Right.
'''
import numpy as np

filename = 'rosalind_ba5b.txt'

def longest_path(n, m, down, right):
	# n+1 rows, m+1 cols
	# assumes that valid paths can only go down or
	weights = np.zeros((n+1, m+1), dtype=int)
	# precalculate right col and bottom row to avoid having to check for out of bounds later
	for r in range(n - 1, -1, -1):
		weights[r, m] = weights[r+1, m] + down[r, m]
	for c in range(m - 1, -1, -1):
		weights[n, c] = weights[n, c+1] + right[n, c]

	# calculate the rest of the grid
	for c in range(m - 1, -1, -1):
		for r in range(n - 1, -1, -1):
			weights[r, c] = max(
				weights[r, c+1] + right[r, c],
				weights[r+1, c] + down[r, c]
				)

	return weights[0, 0]

def main():
	with open(filename) as f:
		n, m = list(map(int, f.readline().strip().split()))
		down, right = [], []
		for i in range(n):
			down.append(list(map(int, f.readline().strip().split())))
		f.readline()
		for i in range(n+1):
			right.append(list(map(int, f.readline().strip().split())))
		down = np.array(down)
		right = np.array(right)
		print(longest_path(n, m, down, right))

if __name__ == '__main__':
	main()
