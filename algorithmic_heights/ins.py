'''
Insertion Sort
http://rosalind.info/problems/ins/

Given: A positive integer n≤103 and an array A[1..n] of integers.

Return: The number of swaps performed by insertion sort algorithm on A[1..n].
'''
filename = 'rosalind_ins.txt'

def insertion_sort_swaps(A):
	swaps = 0
	for i in range(1, len(A)):
		k = i
		while k and A[k] < A[k-1]:
			A[k], A[k-1] = A[k-1], A[k]
			k -= 1
			swaps += 1
	return swaps

def main():
	with open(filename) as f:
		f.readline() # discard--this is just len(A)
		A = [int(i) for i in f.readline().strip().split()]
	print(insertion_sort_swaps(A))

if __name__ == '__main__':
	main()
