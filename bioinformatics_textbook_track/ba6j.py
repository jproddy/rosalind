'''
Implement 2-BreakOnGenomeGraph
http://rosalind.info/problems/ba6j/

Given: The colored edges of a genome graph GenomeGraph, followed by indices i, i', j, and j'.

Return: The colored edges of the genome graph resulting from applying the 2-break operation.
'''
filename = 'rosalind_ba6j.txt'

def two_break_on_genome_graph(genome_graph, i, i_p, j, j_p):
	genome_graph.remove((i, i_p))
	genome_graph.remove((j, j_p))
	genome_graph.add((i, j))
	genome_graph.add((i_p, j_p))
	return genome_graph

def main():
	with open(filename) as f:
		genome_graph = set(eval(f.readline()))
		i, i_p, j, j_p = eval(f.readline())
	print(', '.join(str(i) for i in two_break_on_genome_graph(genome_graph, i, i_p, j, j_p)))

if __name__ == '__main__':
	main()
