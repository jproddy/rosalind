'''
The Wright-Fisher Model of Genetic Drift
http://rosalind.info/problems/wfmd/

Given: Positive integers N (N≤7), m (m≤2N), g (g≤6) and k (k≤2N).

Return: The probability that in a population of N diploid individuals initially possessing m copies of a dominant allele, we will observe after g generations at least k copies of a recessive allele. Assume the Wright-Fisher model.
'''
import numpy as np
from aspc import nCr

filename = 'rosalind_wfmd.txt'

def wr_drift(N, m, g, k):
	dom = m / (2 * N)
	rec = 1 - dom
	# calculate distribution of dominant alleles in given generation
	gen = np.array([nCr(2*N, i) * rec**i * dom**(2*N-i) for i in range(2*N+1)])
	# generate transition matrix
	transition_matrix = np.array([[nCr(2*N, j) * (i/(2*N))**j * (1-(i/(2*N)))**(2*N-j) for j in range(2*N+1)] for i in range(2*N+1)])
	# multiply each generational distribution by the transition matrix
	for _ in range(g - 1):
		gen = gen.dot(transition_matrix)
	return sum(gen[k:])

def main():
	with open(filename) as f:
		N, m, g, k = [int(i) for i in f.readline().strip().split()]
	print(wr_drift(N, m, g, k))

if __name__ == '__main__':
	main()
