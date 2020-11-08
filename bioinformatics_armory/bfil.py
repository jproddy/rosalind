'''
Base Filtration by Quality
http://rosalind.info/problems/bfil/

Given: FASTQ file, quality cut-off value q, Phred33 quality score assumed.

Return: FASTQ file trimmed from the both ends (removed leading and trailing bases with quality lower than q)
'''
import numpy as np
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from io import StringIO

filename = 'rosalind_bfil.txt'

def trimmed_fastq(fastq, threshold_q):
	new_fastq = []
	for record in SeqIO.parse(StringIO(fastq), 'fastq'):
		id_ = record.id # is this distinct from record.name?
		seq = record.seq
		annot = record.letter_annotations['phred_quality']

		start, end = 0, len(seq)
		for i, q in enumerate(annot):
			if q >= threshold_q:
				start = i
				break
		for i, q in enumerate(reversed(annot)):
			if q >= threshold_q:
				end = len(seq) - i
				break

		new_record = SeqRecord(
            seq=seq[start:end],
            id=id_,
            description='',
			letter_annotations={'phred_quality': annot[start:end]}
        )
		new_fastq.append(new_record.format('fastq'))

	return ''.join(new_fastq)

def main():
	with open(filename) as f:
		threshold_q = float(f.readline().strip())
		fastq = f.read()
	print(trimmed_fastq(fastq, threshold_q))

if __name__ == '__main__':
	main()
