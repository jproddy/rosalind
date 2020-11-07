'''
Read Filtration by Quality
http://rosalind.info/problems/filt/

Given: A quality threshold value q, percentage of bases p, and set of FASTQ entries.

Return: Number of reads in filtered FASTQ entries
'''
from Bio import SeqIO
from io import StringIO

filename = 'rosalind_filt.txt'

def sufficient_quality_reads(fastq, threshold_q, threshold_p):
	n_sufficient = 0
	for record in SeqIO.parse(StringIO(fastq), 'fastq'):
		sufficient_q = [i >= threshold_q for i in record.letter_annotations['phred_quality']]
		n_sufficient += (sum(sufficient_q) / len(sufficient_q)) >= (threshold_p / 100)
	return n_sufficient

def main():
	with open(filename) as f:
		threshold_q, threshold_p = tuple(map(float, f.readline().strip().split()))
		fastq = f.read()
	print(sufficient_quality_reads(fastq, threshold_q, threshold_p))

if __name__ == '__main__':
	main() 
