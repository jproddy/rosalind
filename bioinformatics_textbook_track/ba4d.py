'''
Compute the Number of Peptides of Given Total Mass
http://rosalind.info/problems/ba4d/

Given: An integer m.

Return: The number of linear peptides having integer mass m.
'''
from collections import Counter

from utils.monoisotopic_mass_table import int_immt

filename = 'rosalind_ba4d.txt'

def n_peptides(m):
	arr = [1] + ([0] * m)
	masses = Counter(int_immt.keys())
	for i in range(min(masses), m + 1):
		arr[i] = sum([count * arr[i-mass] for mass, count in masses.items() if (i - mass) >= 0])
	return arr[m]

def main():
	with open(filename) as f:
		m = int(f.readline().strip())
	print(n_peptides(m))

if __name__ == '__main__':
	main()
