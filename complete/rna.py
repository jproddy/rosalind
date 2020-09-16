'''
Transcribing DNA into RNA
http://rosalind.info/problems/rna/

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
'''
filename = 'rosalind_rna.txt'

def convert_to_rna(dna):
	return dna.replace('T', 'U')
	# alternatively, with list comprehension:
	# return ''.join([base if base != 'T' else 'U' for base in dna])

def main():
	with open(filename) as f:
		dna = f.readline().strip()
	rna = convert_to_rna(dna)
	print(rna)

if __name__ == '__main__':
	main()
