'''
2-Way Partition
http://rosalind.info/problems/par/

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: A permuted array B[1..n] such that it is a permutation of A and there is an index 1≤q≤n such that B[i]≤A[1] for all 1≤i≤q−1, B[q]=A[1], and B[i]>A[1] for all q+1≤i≤n.
'''
filename = 'rosalind_par.txt'

def partition(A):
	# partitions A inplace as described
	pivot, i = A[0], 0
	hi_i = len(A) - 1
	while i + 1 < hi_i:
		if A[i+1] > pivot:
			A[i+1], A[hi_i] = A[hi_i], A[i+1]
			hi_i -= 1
		else:
			A[i], A[i+1] = A[i+1], A[i]
			i += 1

def main():
	with open(filename) as f:
		f.readline() # discard--len(A)
		A = [int(i) for i in f.readline().strip().split()]
	partition(A)
	print(' '.join([str(i) for i in A]))

	

if __name__ == '__main__':
	main()
