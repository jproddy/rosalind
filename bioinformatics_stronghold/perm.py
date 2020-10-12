'''
Enumerating Gene Orders
http://rosalind.info/problems/perm/

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
'''
from itertools import permutations

filename = 'rosalind_perm.txt'

def perm(n):
	return list(permutations(range(1, n+1)))
	# alternatively, heap's algorithm:
	# perms = []
	# def helper(k, arr):
	# 	if k == 1:
	# 		perms.append(arr.copy())
	# 	else:
	# 		helper(k-1, arr)
	# 		for i in range(k-1):
	# 			if k & 1:
	# 				arr[0], arr[-1] = arr[-1], arr[0]
	# 			else:
	# 				arr[i], arr[-1] = arr[-1], arr[i]
	# 			helper(k-1, arr)		
	# helper(n, list(range(1, n+1)))
	# return perms

def main():
	with open(filename) as f:
		n = int(f.readline().strip())
	perms = perm(n)
	print(len(perms))
	print('\n'.join([' '.join(str(n) for n in i) for i in perms]))

if __name__ == '__main__':
	main()
