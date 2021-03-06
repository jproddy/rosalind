'''
Catalan Numbers and RNA Secondary Structures
http://rosalind.info/problems/cat/

Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.

Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, modulo 1,000,000.
'''
from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_cat.txt'
memo = {}
bp = {
	'A': 'U',
	'C': 'G',
	'G': 'C',
	'U': 'A',
}

def populate_memo():
	# generate base cases
	bases = ['A', 'C', 'G', 'U']
	for i in bases:
		for j in bases:
			if i == bp[j]:
				memo[i+j] = 1
			else:
				memo[i+j] = 0
	print(memo)

def cat(s):
	if len(s) == 0:
		return 1
	elif s in memo:
		pass
	else:		
		total = 0
		for i in range(1, len(s), 2):
			if s[0] == bp[s[i]]:
				total += cat(s[1:i]) * cat(s[i+1:])
		memo[s] = total
	return memo[s]

def main():
	with open(filename) as f:
		fasta = f.read()
	rna = parse_fasta_as_list(fasta)[0]
	populate_memo()
	print(cat(rna) % 1000000)
	
if __name__ == '__main__':
	main()
