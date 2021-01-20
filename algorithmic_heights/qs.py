'''
Quick Sort
http://rosalind.info/problems/qs/

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: A sorted array A[1..n].
'''
import random

filename = 'rosalind_qs.txt'

def quick_sort(A):
	if len(A) <= 1:
		return A
	pivot = random.choice(A) # could also just choose first or last or mid etc.
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
	A[:lo_i] = quick_sort(A[:lo_i])
	A[i:] = quick_sort(A[i:])
	return A

def main():
	with open(filename) as f:
		f.readline()
		A = list(map(int, f.readline().strip().split()))
	print(*quick_sort(A))

if __name__ == '__main__':
	main()
