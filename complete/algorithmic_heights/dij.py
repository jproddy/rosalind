'''
Dijkstra's Algorithm
http://rosalind.info/problems/dij/

Given: A simple directed graph with positive edge weights from 1 to 103 and n≤103 vertices in the edge list format.

Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). If i is not reachable from 1 set D[i] to −1.
'''
filename = 'rosalind_dij.txt'

def dijkstra(n_vertices, edges):
	adj_list = directed_weighted_adjacency_list(n_vertices, edges)
	unvisited = {i for i in range(1, n_vertices+1)}
	dist = [0] + [float('inf')] * (n_vertices-1)
	while unvisited:
		curr = min(unvisited, key=lambda x: dist[x-1])
		unvisited.remove(curr)
		for neighbor in adj_list[curr]:
			if neighbor[0] in unvisited and (dist[curr-1] + neighbor[1]) < dist[neighbor[0]-1]:
				dist[neighbor[0]-1] = dist[curr-1] + neighbor[1]
	return [i if i != float('inf') else -1 for i in dist]

def directed_weighted_adjacency_list(n_vertices, edges):
	adj_list = {i: [] for i in range(1, n_vertices+1)}
	for edge in edges:
		adj_list[edge[0]].append(edge[1:])
	return adj_list

def main():
	with open(filename) as f:
		n_vertices = int(f.readline().strip().split()[0])
		edges = [[int(i) for i in line.strip().split()] for line in f.readlines()]
	print(' '.join(str(i) for i in dijkstra(n_vertices, edges)))

if __name__ == '__main__':
	main()
