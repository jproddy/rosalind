'''
Heap Sort
http://rosalind.info/problems/hs/

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: A sorted array A.
'''
from hea import heapify

filename = 'rosalind_hs.txt'

def heap_sort(A):
	heapify(A)
	for end_heap in range(len(A)-1, 0, -1):
		A[0], A[end_heap] = A[end_heap], A[0]
		bubble_down(A, end_heap, 0)
	return A

def bubble_down(A, end_heap, i):
	l, r = i * 2 + 1, i * 2 + 2
	if r < end_heap: # both children exist
		if A[l] > A[i] and A[l] >= A[r]: # left child is greater
			A[i], A[l] = A[l], A[i]
			bubble_down(A, end_heap, l)
		elif A[r] > A[i] and A[r] > A[l]: # right child is greater
			A[i], A[r] = A[r], A[i]
			bubble_down(A, end_heap, r)
	elif l < end_heap and A[l] > A[i]:
		A[i], A[l] = A[l], A[i]
		bubble_down(A, end_heap, l)

def main():
	with open(filename) as f:
		f.readline() # discard--len(A)
		A = [int(i) for i in f.readline().strip().split()]
	print(' '.join([str(i) for i in heap_sort(A)]))

if __name__ == '__main__':
	main()
