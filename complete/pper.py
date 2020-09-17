'''
Partial Permutations
http://rosalind.info/problems/pper/

Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.

Return: The total number of partial permutations P(n,k), modulo 1,000,000
'''
from functools import reduce

filename = 'rosalind_pper.txt'

def partial_permutations(n, k):
	# n! / (n-k)!
	return reduce(lambda x, y: x * y, range(n-k+1, n+1), 1)

def main():
	with open(filename) as f:
		line = f.readline()
	n, k = [int(i) for i in line.split()]
	print(partial_permutations(n, k) % 1000000)

if __name__ == '__main__':
	main()
