'''
Overlap Graphs
http://rosalind.info/problems/grph/

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
'''
from utils.parse_fasta import parse_fasta_as_dict

filename = 'rosalind_grph.txt'

def adjacency_list_o3(dnas):
	overlaps = []
	for key1, dna1 in dnas.items():
		for key2, dna2 in dnas.items():
			if key1 != key2 and dna1[-3:] == dna2[:3]:
				overlaps.append((key1, key2))
	return overlaps

def main():
	with open(filename) as f:
		fasta = f.read()
	dnas = parse_fasta_as_dict(fasta)
	print('\n'.join([' '.join(pair) for pair in adjacency_list_o3(dnas)]))

if __name__ == '__main__':
	main()
