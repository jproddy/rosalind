'''
Enumerating Oriented Gene Orderings
http://rosalind.info/problems/sign/

Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).
'''
import numpy as np
from itertools import permutations

filename = 'rosalind_sign.txt'

def signed_permutations(n):
	perms = np.array(list(permutations(range(1, n+1))))
	signs = []
	def sign_helper(curr=[]):
		if len(curr) == n:
			signs.append(curr.copy())
		else:
			for sign in [1, -1]:
				sign_helper(curr + [sign])
	sign_helper()
	signs = np.array(signs)
	return [p * s for p in perms for s in signs]

def main():
	with open(filename) as f:
		n = int(f.readline().strip())
	signed_perms = signed_permutations(n)
	# print(signed_perms)
	print(len(signed_perms))
	print('\n'.join([' '.join(str(i) for i in sp) for sp in signed_perms]))

if __name__ == '__main__':
	main()
