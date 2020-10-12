'''
Matching Random Motifs
http://rosalind.info/problems/rstr/

Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.

Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x (see “Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random string to be created more than once.
'''
from collections import Counter

filename = 'rosalind_rstr.txt'

def p_random_strings(n, x, dna):
	count = Counter(dna)
	gc = count['G'] + count['C']
	at = count['A'] + count['T']
	return 1 - (1 - ((1-x)/2)**at * (x/2)**(gc)) ** n

def main():
	with open(filename) as f:
		line = f.readline().strip().split()
		dna = f.readline().strip()
	n, x = int(line[0]), float(line[1])
	print(p_random_strings(n, x, dna))

if __name__ == '__main__':
	main()
