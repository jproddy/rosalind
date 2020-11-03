'''
Error Correction in Reads
http://rosalind.info/problems/corr/

Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read s in the dataset, one of the following applies:

s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).
Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)
'''
from utils.parse_fasta import parse_fasta_as_list
from revc import reverse_complement
from hamm import hamming_distance

filename = 'rosalind_corr.txt'

def error_corrections(reads):
	# seen contains only the read, seen_twice contains both the read and its reverse complement
	seen, seen_twice = set(), set()
	corrections = {}
	
	for read in reads:
		read_revc = reverse_complement(read)
		if read in seen_twice:
			continue
		elif read in seen or read_revc in seen:
			seen.discard(read)
			seen.discard(read_revc)
			seen_twice.add(read)
			seen_twice.add(read_revc)
		else:
			seen.add(read)

	for i in seen:
		for j in seen_twice:
			if hamming_distance(i, j) == 1:
				corrections[i] = j
				break

	return corrections

def main():
	with open(filename) as f:
		fasta = f.read()
	reads = parse_fasta_as_list(fasta)
	corrections = error_corrections(reads)
	for old_read, new_read in corrections.items():
		print(f'{old_read}->{new_read}')

if __name__ == '__main__':
	main()
