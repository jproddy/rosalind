'''
Testing Bipartiteness
http://rosalind.info/problems/bip/

Given: A positive integer k≤20 and k simple graphs in the edge list format with at most 103 vertices each.

Return: For each graph, output "1" if it is bipartite and "-1" otherwise.
'''
import sys
from ddeg import adjacency_list

# hit recursion limit with default settings--probably a cleaner way to solve this?
sys.setrecursionlimit(1500)

filename = 'rosalind_bip.txt'

def bipartite(edge_list, n_vert_list):
	adj_lists = [adjacency_list(edges, n_vertices) for edges, n_vertices in zip(edge_list, n_vert_list)]
	return [1 if is_bipartite(adj_list) else -1 for adj_list in adj_lists]

def is_bipartite(adj_list):
	# uses dfs to generate a two-coloring of the graph and returns the valididy
	colors = {}

	def dfs(vertex, curr_color):
		if vertex in colors:
			if colors[vertex] != curr_color:
				return False
		else:
			colors[vertex] = curr_color
			return all([dfs(neighbor, int(not bool(curr_color))) for neighbor in adj_list[vertex]])
		return True

	return all([dfs(vertex, colors.get(vertex, 0)) for vertex in adj_list])

def main():
	with open(filename) as f:
		graphs = f.read().strip().split('\n\n')[1:]
	edge_list, n_vert_list = [], []
	for graph in graphs:
		lines = graph.split('\n')
		n_vert_list.append(int(lines[0].split()[0]))
		edge_list.append([[int(i) for i in line.strip().split()] for line in lines[1:]])
	print(' '.join([str(i) for i in bipartite(edge_list, n_vert_list)]))

if __name__ == '__main__':
	main()
