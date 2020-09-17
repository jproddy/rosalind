'''
RNA Splicing
http://rosalind.info/problems/splc/

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
'''
from utils.parse_fasta import parse_fasta_as_list
import rna, prot

filename = 'rosalind_splc.txt'

def splice(dnas):
	exon = max(dnas, key=len)
	introns = dnas.copy()
	introns.remove(exon)
	for intron in introns:
		exon = exon.replace(intron, '')
	return prot.translate(rna.convert_to_rna(exon), stop='*')

def main():
	with open(filename) as f:
		fasta = f.read()
	dnas = parse_fasta_as_list(fasta)
	print(splice(dnas)[:-1]) # exclude terminal stop

if __name__ == '__main__':
	main()
