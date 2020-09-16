'''
Calculating Expected Offspring
http://rosalind.info/problems/iev/

Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
'''
import numpy as np

filename = 'rosalind_iev.txt'

def expected_dominant(parent_genotypes):
	# AA x AA | AA x Aa | AA x aa | Aa x Aa | Aa x aa | aa x aa
	ratio_dominant_child = np.array([1, 1, 1, 0.75, 0.5, 0])
	return 2 * sum(parent_genotypes * ratio_dominant_child)
	# alternatively, without numpy array, multiply item by item:
	# ratio_dominant_child = [1, 1, 1, 0.75, 0.5, 0]
	# return 2 * sum([pg * rdc for pg, rdc in zip(parent_genotypes, ratio_dominant_child)])

def main():
	with open(filename) as f:
		line = f.readline().strip()
	# AA x AA | AA x Aa | AA x aa | Aa x Aa | Aa x aa | aa x aa
	parent_genotypes = np.array([int(genotype) for genotype in line.split()])
	print(expected_dominant(parent_genotypes))

if __name__ == '__main__':
	main()
