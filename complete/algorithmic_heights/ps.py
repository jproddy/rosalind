'''
Partial Sort
http://rosalind.info/problems/ps/

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105, a positive integer k≤1000.

Return: The k smallest elements of a sorted array A.
'''
filename = 'rosalind_ps.txt'

def partial_sort(A, k):
	min_heapify(A)
	for end_heap in range(len(A)-1,len(A)-k-2, -1):
		A[0], A[end_heap] = A[end_heap], A[0]
		bubble_down(A, end_heap, 0)
	return reversed(A[-k:])

def min_heapify(A):
	for i in range((len(A)-1)//2, -1, -1):
		bubble_down(A, len(A)-1, i)
	return A

def bubble_down(A, end_heap, i):
	l, r = i * 2 + 1, i * 2 + 2
	if r < end_heap: # both children exist
		if A[l] < A[i] and A[l] <= A[r]: # left child is greater
			A[i], A[l] = A[l], A[i]
			bubble_down(A, end_heap, l)
		elif A[r] < A[i] and A[r] < A[l]: # right child is greater
			A[i], A[r] = A[r], A[i]
			bubble_down(A, end_heap, r)
	elif l < end_heap and A[l] < A[i]: # only left child exists
		A[i], A[l] = A[l], A[i]
		bubble_down(A, end_heap, l)

def main():
	with open(filename) as f:
		f.readline() # discard--len(A)
		A = [int(i) for i in f.readline().strip().split()]
		k = int(f.readline().strip())
	print(' '.join([str(i) for i in partial_sort(A, k)]))

if __name__ == '__main__':
	main()
