'''
Implement ColoredEdges
http://rosalind.info/problems/ba6h/

Given: A genome P.

Return: The collection of colored edges in the genome graph of P in the form (x, y).
'''
from ba6f import chromosome_to_cycle

filename = 'rosalind_ba6h.txt'

def colored_edges(P):
	edges = set()
	for chromosome in P:
		nodes = chromosome_to_cycle(chromosome)
		for j in range(1, len(chromosome)):
			edges.add((nodes[2*j-1], nodes[2*j]))
		edges.add((nodes[-1], nodes[0]))
	return edges

def main():
	with open(filename) as f:
		P = [
			list(map(int, chromosome.split()))
			for chromosome in f.readline().strip()[1:-1].split(')(')
		]
	print(*colored_edges(P), sep=', ')

if __name__ == '__main__':
	main()
