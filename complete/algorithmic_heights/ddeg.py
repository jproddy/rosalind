'''
Double-Degree Array
http://rosalind.info/problems/ddeg/

Given: A simple graph with n≤103 vertices in the edge list format.

Return: An array D[1..n] where D[i] is the sum of the degrees of i's neighbors.
'''
filename = 'rosalind_ddeg.txt'

def adjacency_list(edges, n_vertices):
	adj_list = {i: [] for i in range(1, n_vertices+1)}
	for edge in edges:
		adj_list[edge[0]] = adj_list.get(edge[0], []) + [edge[1]]
		adj_list[edge[1]] = adj_list.get(edge[1], []) + [edge[0]]
	return adj_list

def neighbors_degrees(edges, n_vertices):
	adj_list = adjacency_list(edges, n_vertices)
	return {vertex: sum([len(adj_list[neighbor]) for neighbor in neighbors]) \
				for vertex, neighbors in adj_list.items()}

def main():
	with open(filename) as f:
		n_vertices = int(f.readline().strip().split()[0])
		edges = [[int(i) for i in line.strip().split()] for line in f.readlines()]
	neighbor_degrees = neighbors_degrees(edges, n_vertices)
	print(' '.join([str(neighbor_degrees[i]) for i in range(1, n_vertices+1)]))

if __name__ == '__main__':
	main()
