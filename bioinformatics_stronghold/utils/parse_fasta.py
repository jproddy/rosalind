'''
parse FASTA files and return as
	a list of strings or
	a dictionary in the form {FASTA ID: string}
'''

def parse_fasta_as_list(fasta_file):
	strings = fasta_file.split('>')[1:]
	return [line[line.index('\n')+1:].replace('\n', '') for line in strings]

def parse_fasta_as_dict(fasta_file):
	strings = fasta_file.split('>')[1:]
	print(strings)
	d = {}
	for line in strings:
		sep = line.index('\n')
		d[line[:sep]] = line[sep+1:].replace('\n', '')
	return d
