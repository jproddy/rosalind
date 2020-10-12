'''
Calculating Protein Mass
http://rosalind.info/problems/prtm/

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.
'''
from utils.monoisotopic_mass_table import mmt

filename = 'rosalind_prtm.txt'

def calc_protein_mass(protein):
	return sum([mmt[aa] for aa in protein])

def main():
	with open(filename) as f:
		protein = f.readline().strip()
	print(calc_protein_mass(protein))

if __name__ == '__main__':
	main()
