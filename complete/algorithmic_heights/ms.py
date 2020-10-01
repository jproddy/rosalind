'''
Merge Sort
http://rosalind.info/problems/ms/

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: A sorted array A[1..n].
'''
from mer import merge_arrays
filename = 'rosalind_ms.txt'

def merge_sort(A):
	if len(A) == 1:
		return A
	mid = len(A) // 2
	left = merge_sort(A[:mid])
	right = merge_sort(A[mid:])
	return merge_arrays(left, right)

def main():
	with open(filename) as f:
		f.readline() # discard--len(A)
		A = [int(i) for i in f.readline().strip().split()]
	print(' '.join([str(i) for i in merge_sort(A)]))

if __name__ == '__main__':
	main()
