'''
Data Formats
http://rosalind.info/problems/frmt/

Given: A collection of n (n≤10) GenBank entry IDs.

Return: The shortest of the strings associated with the IDs in FASTA format.
'''
from Bio import Entrez, SeqIO

from secret.email import email

filename = 'rosalind_frmt.txt'

def shortest_string(ids):
	Entrez.email = email
	id_query = ' ,'.join(ids)
	handle = Entrez.efetch(db='nucleotide', id=id_query, rettype='fasta')
	records = handle.read()
	records = [record for record in records.split('\n\n') if record]
	return min(records, key=len)

def main():
	with open(filename) as f:
		ids = f.readline().strip().split()
	print(shortest_string(ids))

if __name__ == '__main__':
	main()
