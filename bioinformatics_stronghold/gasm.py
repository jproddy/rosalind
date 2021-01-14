'''
Genome Assembly Using Reads
http://rosalind.info/problems/gasm/

Given: A collection S of (error-free) reads of equal length (not exceeding 50 bp). In this dataset, for some positive integer k, the de Bruijn graph Bk on Sk+1∪Srck+1 consists of exactly two directed cycles.

Return: A cyclic superstring of minimal length containing every read or its reverse complement.
'''
from pcov import de_brujin_adjacency_dict
from revc import reverse_complement

filename = 'rosalind_gasm.txt'

def setup_assemble_genome(S):
	reads = set(S) | {reverse_complement(i) for i in S}
	while True:
		genome = assemble_genome(reads)
		if genome:
			return genome
		else:
			reads = {read[:-1] for read in reads} | {read[1:] for read in reads}

def assemble_genome(dnas):
	# similar to pcov
	genome = dnas.copy().pop()
	len_kmer = len(genome)
	adj_dict = de_brujin_adjacency_dict(dnas)
	while True:
		if genome[-len_kmer+1:] in adj_dict:
			genome += adj_dict[genome[-len_kmer+1:]][-1]
		else:
			return ''
		if len(genome) == len(dnas) // 2:
			return genome

def main():
	with open(filename) as f:
		S = [line.strip() for line in f.readlines()]
	print(setup_assemble_genome(S))

if __name__ == '__main__':
	main()
