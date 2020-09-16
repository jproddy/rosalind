'''
parse FASTA files and return as
	a list of strings or
	a dictionary in the form {FASTA ID: string}

13, 14 in the code correspond to the known header format:
	>Rosalind_xxxx
'''

def parse_fasta_as_list(fasta_file):
	strings = fasta_file.split('>')[1:]
	return [line[14:].replace('\n', '') for line in strings]

def parse_fasta_as_dict(fasta_file):
	strings = fasta_file.split('>')[1:]
	return {line[:13]: line[14:].replace('\n', '') for line in strings}
