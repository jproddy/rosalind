'''
3SUM
http://rosalind.info/problems/3sum/

Given: A positive integer k≤20, a postive integer n≤104, and k arrays of size n containing integers from −105 to 105.

Return: For each array A[1..n], output three different indices 1≤p<q<r≤n such that A[p]+A[q]+A[r]=0 if exist, and "-1" otherwise.
'''
filename = 'rosalind_3sum.txt'

def three_sums(arrs):
	# solved in O(n^2), but somewhat more efficient (and substantially more complicated)
	# solutions exist: https://en.wikipedia.org/wiki/3SUM
	return [helper(arr) for arr in arrs]

def helper(arr):
	seen = {val: i for i, val in enumerate(arr)}
	for i in range(len(arr)-1):
		print(i)
		for j in range(i+1, len(arr)):
			desired = -(arr[i] + arr[j])
			if desired in seen and seen[desired] != i and seen[desired] != j:
				return sorted([seen[desired]+1, i+1, j+1]) # offset by 1 because 1-indexed
	return [-1]

def main():
	with open(filename) as f:
		f.readline() # discard--number and length of arrays
		arrs = [[int(i) for i in line.strip().split()] for line in f.readlines()]
	print('\n'.join([' '.join([str(i) for i in line]) for line in three_sums(arrs)]))

if __name__ == '__main__':
	main()
