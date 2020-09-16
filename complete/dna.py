'''
Counting DNA Nucleotides
http://rosalind.info/problems/dna/

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''
from collections import Counter

filename = 'rosalind_dna.txt'

def count_bases(dna):
	return Counter(dna)
	# alternatively, can manually count:
	# bases = {
	# 	'A': 0,
	# 	'C': 0,
	# 	'G': 0,
	# 	'T': 0,
	# }
	# for base in dna:
	# 	bases[base] += 1
	# return bases

def main():
	with open(filename) as f:
		dna = f.readline().strip()
	bases = count_bases(dna)
	print(bases['A'], bases['C'], bases['G'], bases['T'])

if __name__ == '__main__':
	main()
