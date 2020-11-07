'''
Read Quality Distribution
http://rosalind.info/problems/phre/

Given: A quality threshold, along with FASTQ entries for multiple reads.

Return: The number of reads whose average quality is below the threshold.
'''
import numpy as np
from Bio import SeqIO
from io import StringIO

filename = 'rosalind_phre.txt'

def insufficient_quality_reads(fastq, threshold_q):
	n_insufficient = 0
	for record in SeqIO.parse(StringIO(fastq), 'fastq'):
		n_insufficient += np.mean(record.letter_annotations['phred_quality']) < threshold_q
	return n_insufficient

def main():
	with open(filename) as f:
		threshold_q = float(f.readline().strip())
		fastq = f.read()
	print(insufficient_quality_reads(fastq, threshold_q))

if __name__ == '__main__':
	main()
