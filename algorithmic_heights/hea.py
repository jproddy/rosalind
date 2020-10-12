'''
Building A Heap
http://rosalind.info/problems/hea/

Given: A positive integer n≤105 and array A[1..n] of integers from −105 to 105.

Return: A permuted array A satisfying the binary max heap property: for any 2≤i≤n, A[⌊i/2⌋]≥A[i].
'''
filename = 'rosalind_hea.txt'

def heapify(A):
	for i in range((len(A)-1)//2, -1, -1):
		bubble_down(A, i)
	return A

def bubble_down(A, i):
	l, r = i * 2 + 1, i * 2 + 2
	if r < len(A): # both children exist
		if A[l] > A[i] and A[l] >= A[r]: # left child is greater
			A[i], A[l] = A[l], A[i]
			bubble_down(A, l)
		elif A[r] > A[i] and A[r] > A[l]: # right child is greater
			A[i], A[r] = A[r], A[i]
			bubble_down(A, r)
	elif l < len(A) and A[l] > A[i]:
		A[i], A[l] = A[l], A[i]
		bubble_down(A, l)

def main():
	with open(filename) as f:
		f.readline() # discard--len(A)
		A = [int(i) for i in f.readline().strip().split()]
	print(' '.join([str(i) for i in heapify(A)]))

if __name__ == '__main__':
	main()
