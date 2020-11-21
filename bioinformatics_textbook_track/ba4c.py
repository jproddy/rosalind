'''

http://rosalind.info/problems/ba4c/

Given: An amino acid string Peptide.

Return: Cyclospectrum(Peptide).
'''
from utils.monoisotopic_mass_table import int_mmt

filename = 'rosalind_ba4c.txt'

def cyclospectrum(peptide):
	spectrum = [0]
	l_pep = len(peptide)
	for _ in range(l_pep):
		curr_mass = 0
		for i in range(l_pep - 1):
			curr_mass += int_mmt[peptide[i]]
			spectrum.append(curr_mass)
		peptide = peptide[1:] + peptide[0]
	# add single copy of full spectrum
	spectrum.append(curr_mass + int_mmt[peptide[-2]])
	return sorted(spectrum)

def main():
	with open(filename) as f:
		peptide = f.readline().strip()
	print(*cyclospectrum(peptide))

if __name__ == '__main__':
	main()
