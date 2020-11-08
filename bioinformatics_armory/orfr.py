'''
Finding Genes with ORFs
http://rosalind.info/problems/orfr/

Given: A DNA string s of length at most 1 kbp.

Return: The longest protein string that can be translated from an ORF of s. If more than one protein string of maximum length exists, then you may output any solution.
'''
import re
from Bio.Seq import Seq
from io import StringIO

filename = 'rosalind_orfr.txt'

def longest_protein(s):
	longest_protein = ''
	seq = Seq(s)
	seq_rc = seq.reverse_complement()
	regex_pattern = '(M.*?)(\*|$)'

	for i in range(3):
		end = 3 * ((len(s) - i) // 3) + i
		prot = str(seq[i:end].translate())
		prot_rc = str(seq_rc[i:end].translate())
		reads = re.findall(regex_pattern, prot) + re.findall(regex_pattern, prot_rc)
		longest_read = max(reads, key=lambda x: len(x[0]))[0]
		longest_protein = max(longest_protein, longest_read, key=len)

	return longest_protein

def main():
	with open(filename) as f:
		s = f.readline().strip()
	print(longest_protein(s))

if __name__ == '__main__':
	main()
