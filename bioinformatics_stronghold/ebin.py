'''
Wright-Fisher's Expected Behavior
http://rosalind.info/problems/ebin/

Given: A positive integer n (n≤1000000) followed by an array P of length m (m≤20) containing numbers between 0 and 1. Each element of P can be seen as representing a probability corresponding to an allele frequency.

Return: An array B of length m for which B[k] is the expected value of Bin(n,P[k]); in terms of Wright-Fisher, it represents the expected allele frequency of the next generation.
'''
filename = 'rosalind_ebin.txt'

def e_bin(n, P):
	return [n * i for i in P]

def main():
	with open(filename) as f:
		n = int(f.readline().strip())
		P = [float(i) for i in f.readline().strip().split()]
	print(' '.join([str(i) for i in e_bin(n, P)]))

if __name__ == '__main__':
	main()
