'''
Genome Assembly with Perfect Coverage
http://rosalind.info/problems/pcov/

Given: A collection of (error-free) DNA k-mers (k≤50) taken from the same strand of a circular chromosome. In this dataset, all k-mers from this strand of the chromosome are present, and their de Bruijn graph consists of exactly one simple cycle.

Return: A cyclic superstring of minimal length containing the reads (thus corresponding to a candidate cyclic chromosome).
'''
filename = 'rosalind_pcov.txt'

def assemble_genome(dnas):
	len_kmer = len(dnas[0])
	len_genome = len(dnas)
	genome = dnas[0]
	adj_dict = de_brujin_adjacency_dict(dnas)
	while len(genome) < len_genome:
		genome += adj_dict[genome[-len_kmer+1:]][-1]
	return genome

def de_brujin_adjacency_dict(dnas):
	adj_dict = {}
	for dna in dnas:
		adj_dict[dna[:-1]] = dna[1:]
	return adj_dict

def main():
	with open(filename) as f:
		dnas = [line.strip() for line in f.readlines()]
	print(assemble_genome(dnas))

if __name__ == '__main__':
	main()
