'''
Introduction to Alternative Splicing
http://rosalind.info/problems/aspc/

Given: Positive integers n and m with 0≤m≤n≤2000.

Return: The sum of combinations C(n,k) for all k satisfying m≤k≤n, modulo 1,000,000. In shorthand, ∑nk=m(nk).
'''
from functools import reduce

filename = 'rosalind_aspc.txt'

def nCr(n, r):
	r = min(r, n-r)
	mult = lambda x, y: x * y
	num = reduce(mult, range(n-r+1, n+1), 1)
	denom = reduce(mult, range(1, r+1), 1)
	return num // denom

def sum_combinations(n, m):
	return sum(nCr(n, k) for k in range(m, n+1))

def main():
	with open(filename) as f:
		line = f.readline().strip()
	n, m = [int(i) for i in line.split()]
	print(sum_combinations(n, m) % 1000000)

if __name__ == '__main__':
	main()
