'''
Find Substrings of a Genome Encoding a Given Amino Acid String
http://rosalind.info/problems/ba4b/

Given: A DNA string Text and an amino acid string Peptide.

Return: All substrings of Text encoding Peptide (if any such substrings exist).
'''
from utils.codon_table import codons_star_stop
from ba1c import reverse_complement

filename = 'rosalind_ba4b.txt'

def encoding_substrings(text, peptide):
	valid_substrings = []
	revc = reverse_complement(text)
	rna = text.replace('T', 'U')
	rna_revc = revc.replace('T', 'U')
	for offset in range(3):
		translation = translate(rna[offset:])
		translation_revc = translate(rna_revc[offset:])
		l_pep = len(peptide)
		for j in range(len(translation) - l_pep + 1):
			if translation[j:j+l_pep] == peptide:
				valid_substrings.append(text[offset+3*j:offset+3*j+3*l_pep])
			if translation_revc[j:j+l_pep] == peptide:
				valid_substrings.append(reverse_complement(revc[offset+3*j:offset+3*j+3*l_pep]))

	return valid_substrings


	
def translate(pattern):
	return ''.join([codons_star_stop[pattern[3*i:3*i+3]] for i in range(len(pattern) // 3)])

def main():
	with open(filename) as f:
		text = f.readline().strip()
		peptide = f.readline().strip()
	for substring in encoding_substrings(text, peptide):
		print(substring)

if __name__ == '__main__':
	main()
