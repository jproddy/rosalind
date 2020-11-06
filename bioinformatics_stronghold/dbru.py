'''
Constructing a De Bruijn Graph
http://rosalind.info/problems/dbru/

Given: A collection of up to 1000 (possibly repeating) DNA strings of equal length (not exceeding 50 bp) corresponding to a set S of (k+1)-mers.

Return: The adjacency list corresponding to the de Bruijn graph corresponding to S∪Src.
'''
from revc import reverse_complement
filename = 'rosalind_dbru.txt'

def de_brujin_adjacency_list(dnas):
	adj_list = set()
	for dna in dnas:
		revc = reverse_complement(dna)
		adj_list.add((dna[:-1], dna[1:]))
		adj_list.add((revc[:-1], revc[1:]))
	return adj_list

def main():
	with open(filename) as f:
		dnas = [line.strip() for line in f.readlines()]
	for edge in de_brujin_adjacency_list(dnas):
		print(f'({edge[0]}, {edge[1]})')

if __name__ == '__main__':
	main()
