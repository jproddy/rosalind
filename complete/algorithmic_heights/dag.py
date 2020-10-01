'''
Testing Acyclicity
http://rosalind.info/problems/dag/

Given: A positive integer k≤20 and k simple directed graphs in the edge list format with at most 103 vertices and 3⋅103 edges each.

Return: For each graph, output "1" if the graph is acyclic and "-1" otherwise.
'''
from bfs import directed_adjacency_list

filename = 'rosalind_dag.txt'

def acyclic(edge_list, n_vert_list):
	# test acyclicity for each graph in list
	dir_adj_lists = [directed_adjacency_list(edges, n_vertices) for edges, n_vertices in zip(edge_list, n_vert_list)]
	return [1 if is_acyclic(dir_adj_list) else -1 for dir_adj_list in dir_adj_lists]

def is_acyclic(dir_adj_list):
	# an acylic graph necessarily has leaf nodes
	# iteritively trim leaves until graph is empty (acyclic) or still has remaining nodes (cyclic)
	# runs in O(n^2) but more efficient methods probably exist
	set_adj_list = {key: set(val) for key, val in dir_adj_list.items()}.copy()
	changed = True
	while changed:
		changed = False
		# must convert to list to copy iterator--otherwise
		# dictionary changed size during iteration RuntimeError
		for vertex in list(set_adj_list.keys()):
			if len(set_adj_list[vertex]) == 0:
				changed = True
				for vertex2, neighbors2 in set_adj_list.items():
					if vertex in neighbors2:
						neighbors2.remove(vertex)
				set_adj_list.pop(vertex)
	return not bool(len(set_adj_list))

def main():
	with open(filename) as f:
		graphs = f.read().strip().split('\n\n')[1:]
	edge_list, n_vert_list = [], []
	for graph in graphs:
		lines = graph.split('\n')
		n_vert_list.append(int(lines[0].split()[0]))
		edge_list.append([[int(i) for i in line.strip().split()] for line in lines[1:]])
	print(' '.join([str(i) for i in acyclic(edge_list, n_vert_list)]))

if __name__ == '__main__':
	main()
