'''
Complementing a Strand of DNA
http://rosalind.info/problems/rvco/

Given: A collection of n (n≤10) DNA strings.

Return: The number of given strings that match their reverse complements.
'''
from Bio import SeqIO

filename = 'rosalind_rvco.txt'

def n_equals_reverse_complement():
	return sum(record.seq == record.reverse_complement().seq for record in SeqIO.parse(filename, 'fasta'))

def main():
	print(n_equals_reverse_complement())

if __name__ == '__main__':
	main()
