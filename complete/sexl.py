'''
Sex-Linked Inheritance
http://rosalind.info/problems/sexl/

Given: An array A of length n for which A[k] represents the proportion of males in a population exhibiting the k-th of n total recessive X-linked genes. Assume that the population is in genetic equilibrium for all n genes.

Return: An array B of length n in which B[k] equals the probability that a randomly selected female will be a carrier for the k-th gene.
'''
filename = 'rosalind_sexl.txt'

def p_carrier(A):
	return [2 * i * (1-i) for i in A]

def main():
	with open(filename) as f:
		A = [float(i) for i in f.readline().strip().split()]
	print(' '.join([str(i) for i in p_carrier(A)]))

if __name__ == '__main__':
	main()
