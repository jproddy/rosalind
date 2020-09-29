'''
2SUM
http://rosalind.info/problems/2sum/

Given: A positive integer k≤20, a positive integer n≤104, and k arrays of size n containing integers from −105 to 105.

Return: For each array A[1..n], output two different indices 1≤p<q≤n such that A[p]=−A[q] if exist, and "-1" otherwise.
'''
filename = 'rosalind_2sum.txt'

def two_sums(arrs):
	res = []
	for arr in arrs:
		seen = {}
		for i, val in enumerate(arr):
			if -val in seen:
				res.append([seen[-val]+1, i+1]) # offset by 1 because 1-indexed
				break
			elif i == len(arr) - 1:
				res.append([-1])
				break
			else:
				seen[val] = i
	return res

def main():
	with open(filename) as f:
		f.readline() # discard--number and length of arrays
		arrs = [[int(i) for i in line.strip().split()] for line in f.readlines()]
	print('\n'.join([' '.join([str(i) for i in line]) for line in two_sums(arrs)]))


if __name__ == '__main__':
	main()
