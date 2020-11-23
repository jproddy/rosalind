'''
Compute the Score of a Cyclic Peptide Against a Spectrum
http://rosalind.info/problems/ba4f/

Given: An amino acid string Peptide and a collection of integers Spectrum.

Return: The score of Peptide against Spectrum, Score(Peptide, Spectrum).
'''
from utils.monoisotopic_mass_table import int_mmt
from ba4c import cyclospectrum

from collections import Counter

filename = 'rosalind_ba4f.txt'

def score_peptide(peptide, spectrum):
	theoretical_spectrum = Counter(cyclospectrum(peptide))
	experimental_spectrum = Counter(spectrum)
	return sum(min(theoretical_spectrum[peak], experimental_spectrum[peak]) for peak in theoretical_spectrum if peak in experimental_spectrum)

def main():
	with open(filename) as f:
		peptide = f.readline().strip()
		spectrum = list(map(int, f.readline().strip().split()))
	print(score_peptide(peptide, spectrum))

if __name__ == '__main__':
	main()
