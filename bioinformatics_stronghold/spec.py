'''
Inferring Protein from Spectrum
http://rosalind.info/problems/spec/

Given: A list L of n (n≤100) positive real numbers.

Return: A protein string of length n−1 whose prefix spectrum is equal to L (if multiple solutions exist, you may output any one of them). Consult the monoisotopic mass table.
'''
from utils.monoisotopic_mass_table import inverted_mmt

filename = 'rosalind_spec.txt'
ROUND = 5 # monoisotopic mass table is rounded to 5 decimals

def protein_from_mass_spec(prefix_weights):
	return [inverted_mmt[round(prefix_weights[i+1]-prefix_weights[i], ROUND)] for i in range(len(prefix_weights)-1)]

def main():
	with open(filename) as f:
		prefix_weights = [float(line.strip()) for line in f.readlines()]
	print(''.join(protein_from_mass_spec(prefix_weights)))

if __name__ == '__main__':
	main()
