'''
Introduction to Random Strings
http://rosalind.info/problems/prob/

Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.
'''
from collections import Counter
import math

filename = 'rosalind_prob.txt'

def prob(dna, A):
	base_counter = Counter(dna)
	at = base_counter['A'] + base_counter['T']
	cg = base_counter['C'] + base_counter['G']
	return [math.log10(((i/2) ** cg) * (((1-i)/2) ** at)) for i in A]


def main():
	with open(filename) as f:
		dna = f.readline().strip()
		A = [float(i) for i in f.readline().strip().split()]
	print(' '.join([str(i) for i in prob(dna, A)]))

if __name__ == '__main__':
	main()
