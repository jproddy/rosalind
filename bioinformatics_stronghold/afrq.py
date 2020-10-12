'''
Counting Disease Carriers
http://rosalind.info/problems/afrq/

Given: An array A for which A[k] represents the proportion of homozygous recessive individuals for the k-th Mendelian factor in a diploid population. Assume that the population is in genetic equilibrium for all factors.

Return: An array B having the same length as A in which B[k] represents the probability that a randomly selected individual carries at least one copy of the recessive allele for the k-th factor.
'''
import math

filename = 'rosalind_afrq.txt'

def at_least_one_rec(A):
	return [i + 2 * math.sqrt(i) * (1-math.sqrt(i)) for i in A]

def main():
	with open(filename) as f:
		A = [float(i) for i in f.readline().strip().split()]
	print(' '.join([str(i) for i in at_least_one_rec(A)]))

if __name__ == '__main__':
	main()
