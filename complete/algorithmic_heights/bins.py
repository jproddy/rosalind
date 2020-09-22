'''
Binary Search
http://rosalind.info/problems/bins/

Given: Two positive integers n≤105 and m≤105, a sorted array A[1..n] of integers from −105 to 105 and a list of m integers −105≤k1,k2,…,km≤105.

Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.
'''
filename = 'rosalind_bins.txt'

def binary_search_list(A, k):
	return [binary_search(i, A) for i in k]

def binary_search(val, A):
	lo, hi = 0, len(A) - 1
	while lo <= hi:
		mid = (lo + hi) // 2
		if A[mid] > val:
			hi = mid - 1
		elif A[mid] < val:
			lo = mid + 1
		elif A[mid] == val:
			return mid
	return -1

def main():
	with open(filename) as f:
		f.readline() # discard--len(A)
		f.readline() # discard--len(k)
		A = [int(i) for i in f.readline().strip().split()]
		k = [int(i) for i in f.readline().strip().split()]
	print(' '.join([str(i) for i in binary_search_list(A, k)]))

if __name__ == '__main__':
	main()
