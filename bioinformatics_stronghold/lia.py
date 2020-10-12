'''
Independent Alleles
http://rosalind.info/problems/lia/

Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
'''
from scipy.stats import binom
from functools import reduce

filename = 'rosalind_lia.txt'

def p_double_hetero(k, N):
	p = 0.25
	return binom.cdf(2 ** k - N, 2 ** k, 1 - p)

# alternatively, define our own nCr function and manually calculate the cdf of the desired binomial distribution

# def nCr(n, r):
# 	r = min(r, n-r)
# 	mult = lambda x, y: x * y
# 	num = reduce(mult, range(n-r+1, n+1), 1)
# 	denom = reduce(mult, range(1, r+1), 1)
# 	return num / denom

# def p_double_hetero(k, N):
# 	return sum([nCr(2**k, i) * (.25 ** i) * (.75 ** (2**k - i)) for i in range(N, 2**k + 1)])

def main():
	with open(filename) as f:
		line = f.readline().strip()
	k, N = [int(i) for i in line.split()]
	print(p_double_hetero(k, N))

if __name__ == '__main__':
	main()
