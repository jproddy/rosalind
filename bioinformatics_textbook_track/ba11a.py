'''
Construct the Graph of a Spectrum
http://rosalind.info/problems/ba11a/

Given: A space-delimited list of integers Spectrum.

Return: Graph(Spectrum).
'''
from collections import namedtuple

from utils.monoisotopic_mass_table import int_immt

filename = 'rosalind_ba11a.txt'

def graph(spectrum):
	# slight edit of bioinformatics_stronhold/sgra
	Edge = namedtuple('Edge', ['next_mass', 'aa'])
	adj_list = {mass: [] for mass in spectrum}
	max_aa_mass = max(int_immt.keys())
	for i in range(len(spectrum) - 1):
		for j in range(i + 1, len(spectrum)):
			diff = spectrum[j] - spectrum[i]
			if diff in int_immt:
				adj_list[spectrum[i]].append(Edge(spectrum[j], int_immt[diff]))
			elif diff > max_aa_mass:
				break
	return adj_list

def main():
	with open(filename) as f:
		spectrum = [0] + list(map(int, f.readline().strip().split()))
	spectrum_graph = graph(spectrum)
	for key, edges in spectrum_graph.items():
		for edge in edges:
			print(f'{key}->{edge.next_mass}:{edge.aa}')

if __name__ == '__main__':
	main()
