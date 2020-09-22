'''
Breadth-First Search
http://rosalind.info/problems/bfs/

Given: A simple directed graph with n≤103 vertices in the edge list format.

Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). If i is not reachable from 1 set D[i] to −1.
'''
filename = 'rosalind_bfs.txt'

def bfs(edges, n_vertices):
	adj_list = directed_adjacency_list(edges, n_vertices)
	shortest = {i: -1 for i in range(1, n_vertices+1)}
	prev, curr = [1], []
	dist = 0
	while prev:
		for vertex in prev:
			if shortest[vertex] == -1:
				shortest[vertex] = dist
				curr.extend(adj_list[vertex])
		prev, curr = curr, []
		dist += 1
	return shortest

def directed_adjacency_list(edges, n_vertices):
	adj_list = {i: [] for i in range(1, n_vertices+1)}
	for edge in edges:
		adj_list[edge[0]] += [edge[1]]
	return adj_list

def main():
	with open(filename) as f:
		n_vertices = int(f.readline().strip().split()[0])
		edges = [[int(i) for i in line.strip().split()] for line in f.readlines()]
	shortest = bfs(edges, n_vertices)
	print(' '.join([str(shortest[i]) for i in range(1, n_vertices+1)]))

if __name__ == '__main__':
	main()
