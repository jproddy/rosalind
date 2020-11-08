'''
Base Quality Distribution
http://rosalind.info/problems/bphr/

Given: FASTQ file, quality threshold q

Return: Number of positions where mean base quality falls below given threshold
'''
import numpy as np
from Bio import SeqIO
from io import StringIO

filename = 'rosalind_bphr.txt'

def insufficient_quality_positions(fastq, threshold_q):
	arr = np.array([record.letter_annotations['phred_quality'] for \
			record in SeqIO.parse(StringIO(fastq), 'fastq')])
	return sum(arr.mean(axis=0) < threshold_q)

def main():
	with open(filename) as f:
		threshold_q = float(f.readline().strip())
		fastq = f.read()
	print(insufficient_quality_positions(fastq, threshold_q))

if __name__ == '__main__':
	main()
