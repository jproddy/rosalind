'''
Expected Number of Restriction Sites
http://rosalind.info/problems/eval/

Given: A positive integer n (n≤1,000,000), a DNA string s of even length at most 10, and an array A of length at most 20, containing numbers between 0 and 1.

Return: An array B having the same length as A in which B[i] represents the expected number of times that s will appear as a substring of a random DNA string t of length n, where t is formed with GC-content A[i] (see “Introduction to Random Strings”).
'''
from collections import Counter

filename = 'rosalind_eval.txt'

def expected_sites(n, s, A):
	counts = Counter(s)
	gc = counts['G'] + counts['C']
	l = len(s)
	return [(n-l+1) * (i/2)**gc * ((1-i)/2)**(l-gc) for i in A]

def main():
	with open(filename) as f:
		n = int(f.readline().strip())
		s = f.readline().strip()
		A = [float(i) for i in f.readline().strip().split()]
	print(' '.join([str(i) for i in expected_sites(n, s, A)]))

if __name__ == '__main__':
	main()
