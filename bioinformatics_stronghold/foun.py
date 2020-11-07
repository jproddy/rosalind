'''
The Founder Effect and Genetic Drift
http://rosalind.info/problems/foun/

Given: Two positive integers N and m, followed by an array A containing k integers between 0 and 2N. A[j] represents the number of recessive alleles for the j-th factor in a population of N diploid individuals.

Return: An m×k matrix B for which Bi,j represents the common logarithm of the probability that after i generations, no copies of the recessive allele for the j-th factor will remain in the population. Apply the Wright-Fisher model.
'''
import math
import numpy as np

from aspc import nCr

filename = 'rosalind_foun.txt'

def wf_drift(N, m, g, k):
	# slight edit of wfmd.wf_drift to return all generations
	dom = m / (2 * N)
	rec = 1 - dom
	gen = np.array([nCr(2*N, i) * rec**i * dom**(2*N-i) for i in range(2*N+1)])
	transition_matrix = np.array([[nCr(2*N, j) * (i/(2*N))**j * (1-(i/(2*N)))**(2*N-j) for j in range(2*N+1)] for i in range(2*N+1)])

	gen_probs = [math.log10(sum(gen[k:]))]
	for _ in range(g - 1):
		gen = gen.dot(transition_matrix)
		gen_probs.append(math.log10(sum(gen[k:])))
	return gen_probs

def wf_drifts(N, m, A):
	# m here represents number of generations, in wf_drift, it represents number
	# of recessive alleles to remain consistent with wfmd.wf_drift
	return np.array([wf_drift(N, a, m, 2*N) for a in A]).T

def main():
	with open(filename) as f:
		N, m = tuple(map(int, f.readline().strip().split()))
		A = list(map(int, f.readline().strip().split()))
	print('\n'.join([' '.join([str(col) for col in row]) for row in wf_drifts(N, m, A)]))

if __name__ == '__main__':
	main()
