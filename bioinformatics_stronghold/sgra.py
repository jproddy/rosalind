'''
Using the Spectrum Graph to Infer Peptides
http://rosalind.info/problems/sgra/

Given: A list L (of length at most 100) containing positive real numbers.

Return: The longest protein string that matches the spectrum graph of L (if multiple solutions exist, you may output any one of them). Consult the monoisotopic mass table.
'''
from utils.monoisotopic_mass_table import inverted_mmt
from collections import namedtuple

filename = 'rosalind_sgra.txt'
ROUND = 4

def longest_protein(L):
	# assume L i sorted low to high
	rounded_immt = {round(k, ROUND): v for k, v in inverted_mmt.items()}
	max_aa_mass = max(rounded_immt.keys())
	Edge = namedtuple('Edge', ['next_mass', 'aa'])
	adj_list = {i: [] for i in L}
	for i in range(len(L)):
		for j in range(i, len(L)):
			val = round(L[j] - L[i], ROUND)
			if val in rounded_immt:
				adj_list[L[i]].append(Edge(L[j], rounded_immt[val]))
			# assuming masses in L are reasonably distributed, below should
			# substantially reduce runtime in larger datasets
			elif val > max_aa_mass:
				break

	curr_longest_mass = L[-1]
	longest_protein_starting_at = {i: '' for i in L}
	for mass in reversed(L):
		if adj_list[mass]:
			longest_edge = max(adj_list[mass], key=lambda edge: len(longest_protein_starting_at[edge.next_mass])) 
			longest_protein_starting_at[mass] = longest_edge.aa + longest_protein_starting_at[longest_edge.next_mass]
			if len(longest_protein_starting_at[mass]) > len(longest_protein_starting_at[curr_longest_mass]):
				curr_longest_mass = mass
		else:
			longest_protein_starting_at[mass] = ''

	return longest_protein_starting_at[curr_longest_mass]

def main():
	with open(filename) as f:
		L = [float(line.strip()) for line in f.readlines()]
	print(longest_protein(L))

if __name__ == '__main__':
	main()
