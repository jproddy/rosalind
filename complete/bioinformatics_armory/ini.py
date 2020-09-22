'''
Introduction to the Bioinformatics Armory
http://rosalind.info/problems/ini/

Given: A DNA string s of length at most 1000 bp.

Return: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s. Note: You must provide your answer in the format shown in the sample output below.
'''
from collections import Counter

filename = 'rosalind_ini.txt'

def count_bases(dna):
	return Counter(dna)

def main():
	with open(filename) as f:
		dna = f.readline().strip()
	bases = count_bases(dna)
	print(bases['A'], bases['C'], bases['G'], bases['T'])

if __name__ == '__main__':
	main()
