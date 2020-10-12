'''
Independent Segregation of Chromosomes
http://rosalind.info/problems/indc/

Given: A positive integer n≤50.

Return: An array A of length 2n in which A[k] represents the common logarithm of the probability that two diploid siblings share at least k of their 2n chromosomes (we do not consider recombination for now).
'''
import math
from scipy.stats import binom
from aspc import nCr

filename = 'rosalind_indc.txt'

def indc(n):
	return [math.log10(binom.cdf(i, 2*n, 0.5)) for i in range(2*n-1, -1, -1)]
	# alternatively, the below gives slightly different numbers at very small values
	# 	--rounding issues?
	# combos = [nCr(2*n, i) for i in range(1, 2*n+1)]
	# cdf = [sum(combos[i:]) for i in range(len(combos))]
	# power = 0.5 ** (2*n)
	# return [math.log10(i * power) for i in cdf]


def main():
	with open(filename) as f:
		n = int(f.readline().strip())
	print(' '.join([str(i) for i in indc(n)]))

if __name__ == '__main__':
	main()
