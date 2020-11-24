'''
Generate the Theoretical Spectrum of a Linear Peptide
http://rosalind.info/problems/ba4j/

Given: An amino acid string Peptide.

Return: The linear spectrum of Peptide.
'''
from utils.monoisotopic_mass_table import int_mmt

filename = 'rosalind_ba4j.txt'

def linear_spectrum(peptide):
	prefix_mass = [0]
	for aa in peptide:
		prefix_mass.append(prefix_mass[-1] + int_mmt[aa])
	spectrum = [0]
	for i in range(len(prefix_mass) - 1):
		for j in range(i + 1, len(prefix_mass)):
			spectrum.append(prefix_mass[j] - prefix_mass[i])
	return sorted(spectrum)

def main():
	with open(filename) as f:
		peptide = f.readline().strip()
	print(*linear_spectrum(peptide))

if __name__ == '__main__':
	main()
