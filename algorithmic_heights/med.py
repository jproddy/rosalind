'''
Median
http://rosalind.info/problems/med/

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105, a positive number k≤n.

Return: The k-th smallest element of A.
'''
import random

filename = 'rosalind_med.txt'

def median(A, k, n_lower=0):
	# find kth smallest element in-place in linear time
	pivot = random.choice(A)
	lo_i, i, hi_i = 0, 0, len(A) - 1
	while i <= hi_i:
		if A[i] == pivot:
			i += 1
		elif A[i] < pivot:
			A[lo_i], A[i] = A[i], A[lo_i]
			i += 1
			lo_i += 1
		else:
			A[hi_i], A[i] = A[i], A[hi_i]
			hi_i -= 1

	if i + n_lower < k:
		return median(A[i:], k, i + n_lower)
	elif lo_i + n_lower >= k:
		return median(A[:lo_i], k, n_lower)
	else:
		return pivot

def main():
	with open(filename) as f:
		f.readline()
		A = list(map(int, f.readline().split()))
		k = int(f.readline().strip())
	print(median(A, k))

if __name__ == '__main__':
	main()
