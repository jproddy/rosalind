'''
GenBank Introduction
http://rosalind.info/problems/gbk/

Given: A genus name, followed by two dates in YYYY/M/D format.

Return: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.
'''
from Bio import Entrez

filename = 'rosalind_gbk.txt'

def access(genus, start, end):
	Entrez.email = '' # removed
	handle = Entrez.esearch(db='nucleotide', term=f'"{genus}"[Organism] AND ("{start}"[PDAT] : "{end}"[PDAT])')
	record = Entrez.read(handle)
	return record['Count']

def main():
	with open(filename) as f:
		genus = f.readline().strip()
		start = f.readline().strip()
		end = f.readline().strip()
	print(access(genus, start, end))

if __name__ == '__main__':
	main()
