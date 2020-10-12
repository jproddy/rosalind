'''
3-Way Partition
http://rosalind.info/problems/par3/

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: An array B[1..n] such that it is a permutation of A and there are indices 1≤q≤r≤n such that B[i]<A[1] for all 1≤i≤q−1, B[i]=A[1] for all q≤i≤r, and B[i]>A[1] for all r+1≤i≤n.
'''
filename = 'rosalind_par3.txt'

def partition(A):
	pivot = A[0]
	lo_i, i, hi_i = 0, 0, len(A) - 1
	while i < hi_i + 1:
		if A[i] > pivot:
			A[i], A[hi_i] = A[hi_i], A[i]
			hi_i -= 1
		elif A[i] < pivot:
			A[i], A[lo_i] = A[lo_i], A[i]
			lo_i += 1
			i += 1
		else:
			i += 1

def main():
	with open(filename) as f:
		f.readline() # discard--len(A)
		A = [int(i) for i in f.readline().strip().split()]
	partition(A)
	print(' '.join([str(i) for i in A]))

if __name__ == '__main__':
	main()
