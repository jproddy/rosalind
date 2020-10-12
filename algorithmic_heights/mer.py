'''
Merge Two Sorted Arrays
http://rosalind.info/problems/mer/

Given: A positive integer n≤105 and a sorted array A[1..n] of integers from −105 to 105, a positive integer m≤105 and a sorted array B[1..m] of integers from −105 to 105.

Return: A sorted array C[1..n+m] containing all the elements of A and B.
'''
filename = 'rosalind_mer.txt'

def merge_arrays(A, B):
	C = []
	Alen, Blen = len(A), len(B)
	Ai, Bi = 0, 0
	while Ai < Alen and Bi < Blen:
		if A[Ai] < B[Bi]:
			C.append(A[Ai])
			Ai += 1
		else:
			C.append(B[Bi])
			Bi += 1
	if Ai < Alen:
		C.extend(A[Ai:])
	elif Bi < Blen:
		C.extend(B[Bi:])
	return C

def main():
	with open(filename) as f:
		f.readline() # discard--len(A)
		A = [int(i) for i in f.readline().strip().split()]
		f.readline() # discard--len(B)
		B = [int(i) for i in f.readline().strip().split()]
	print(' '.join([str(i) for i in merge_arrays(A, B)]))

if __name__ == '__main__':
	main()
