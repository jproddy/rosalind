'''
Counting Phylogenetic Ancestors
http://rosalind.info/problems/inod/

Given: A positive integer n (3≤n≤10000).

Return: The number of internal nodes of any unrooted binary tree having n leaves.
'''
filename = 'rosalind_inod.txt'

def n_internal_nodes(n):
	return n - 2

def main():
	with open(filename) as f:
		n = int(f.readline().strip())
	print(n_internal_nodes(n))

if __name__ == '__main__':
	main()
