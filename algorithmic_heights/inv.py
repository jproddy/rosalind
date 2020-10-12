'''
Counting Inversions
http://rosalind.info/problems/inv/

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: The number of inversions in A.
'''
filename = 'rosalind_inv.txt'

# the trivial O(n^2) solution:
'''
def inversions(A):
	count = 0
	for i, iv in enumerate(A):
		for jv in A[i:]:
			if iv > jv:
				count += 1
	return count
'''

def inversions(A):
	# mergesorts A and counts inversions in O(n*log(n))
	merged, invs = merge_sort(A)
	return invs 

def merge_sort(A):
	if len(A) == 1:
		return A, 0
	mid = len(A) // 2
	left, left_inv = merge_sort(A[:mid])
	right, right_inv = merge_sort(A[mid:])
	merged, new_inv = merge_arrays(left, right)
	return merged, left_inv + right_inv + new_inv

def merge_arrays(A, B):
	invs = 0
	C = []
	Alen, Blen = len(A), len(B)
	Ai, Bi = 0, 0
	while Ai < Alen and Bi < Blen:
		if A[Ai] <= B[Bi]:
			C.append(A[Ai])
			Ai += 1
		else:
			C.append(B[Bi])
			Bi += 1
			invs += Alen - Ai
	if Ai < Alen:
		C.extend(A[Ai:])
	elif Bi < Blen:
		C.extend(B[Bi:])
	return C, invs

def main():
	with open(filename) as f:
		f.readline() # discard--len(A)
		A = [int(i) for i in f.readline().strip().split()]
	print(inversions(A))
	print(inversions_n2(A))

if __name__ == '__main__':
	main()
