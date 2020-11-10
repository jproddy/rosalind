'''
Find the Reverse Complement of a String
http://rosalind.info/problems/ba1c/

Given: A DNA string Pattern.

Return: Pattern, the reverse complement of Pattern.
'''
filename = 'rosalind_ba1c.txt'

def reverse_complement(s):
	# copied from bioinformatics_stronghold/revc
	complements = {
		'A': 'T',
		'C': 'G',
		'G': 'C',
		'T': 'A',
	}
	return ''.join(complements[base] for base in reversed(s))

def main():
	with open(filename) as f:
		s = f.readline().strip()
	print(reverse_complement(s))

if __name__ == '__main__':
	main()
