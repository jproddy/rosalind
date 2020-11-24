'''
Compute the Score of a Linear Peptide
http://rosalind.info/problems/ba4k/

Given: An amino acid string Peptide and a collection of integers LinearSpectrum.

Return: The linear score of Peptide against Spectrum, LinearScore(Peptide, Spectrum).
'''
from collections import Counter

from ba4j import linear_spectrum

filename = 'rosalind_ba4k.txt'

def linear_score(peptide, spectrum):
	theoretical_spectrum = Counter(linear_spectrum(peptide))
	experimental_spectrum = Counter(spectrum)
	return sum(min(theoretical_spectrum[peak], experimental_spectrum[peak]) for peak in theoretical_spectrum if peak in experimental_spectrum)

def main():
	with open(filename) as f:
		peptide = f.readline().strip()
		spectrum = list(map(int, f.readline().strip().split()))
	print(linear_score(peptide, spectrum))

if __name__ == '__main__':
	main()
