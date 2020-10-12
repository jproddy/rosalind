'''
Complementing a Strand of DNA
http://rosalind.info/problems/revc/

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
'''
filename = 'rosalind_revc.txt'

def reverse_complement(s):
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
	sc = reverse_complement(s)
	print(sc)

if __name__ == '__main__':
	main()
