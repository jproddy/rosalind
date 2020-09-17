'''
Completing a Tree
http://rosalind.info/problems/tree/

Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.
'''
filename = 'rosalind_tree.txt'

def min_additional_edges(n_nodes, adj_list):
	# n nodes must be connected by n-1 edges
	return n_nodes - len(adj_list) - 1

def main():
	with open(filename) as f:
		lines = f.readlines()
	print(min_additional_edges(int(lines[0]), lines[1:]))

if __name__ == '__main__':
	main()
