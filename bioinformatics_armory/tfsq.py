'''
FASTQ format introduction
http://rosalind.info/problems/tfsq/

Given: FASTQ file

Return: Corresponding FASTA records
'''
filename = 'rosalind_tfsq.txt'

def fastq_to_fasta(fastq):
	return '\n'.join([f'>{line[1:]}' if i%4==0 else line for i, line in enumerate(fastq.split('\n')[:-1]) if i%4==0 or i%4==1])

def main():
	with open(filename) as f:
		fastq = f.read()
	print(fastq_to_fasta(fastq))

if __name__ == '__main__':
	main()
