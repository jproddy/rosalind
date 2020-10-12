'''
Open Reading Frames
http://rosalind.info/problems/orf/

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
'''
from utils.parse_fasta import parse_fasta_as_list
from utils.codon_table import codons_star_stop
import rna, revc, prot

filename = 'rosalind_orf.txt'

def open_reading_frames(dna_):
	dnac = revc.reverse_complement(dna_)
	rna_ = rna.convert_to_rna(dna_)
	rnac = rna.convert_to_rna(dnac)
	proteins = []
	for i in range(3):
		proteins.append(prot.translate(rna_[i:], stop='*'))
		proteins.append(prot.translate(rnac[i:], stop='*'))
	candidates = []
	for protein in proteins:
		for i, aa in enumerate(protein):
			if aa == 'M':
				for j, aa_stop in enumerate(protein[i+1:]):
					if aa_stop == '*':
						candidates.append(protein[i:i+j+1])
						break
	return set(candidates)

def main():
	with open(filename) as f:
		fasta = f.read()
	dna = parse_fasta_as_list(fasta)[0]
	print('\n'.join(open_reading_frames(dna)))

if __name__ == '__main__':
	main()
