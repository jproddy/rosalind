'''
Bellman-Ford Algorithm
http://rosalind.info/problems/bf/

Given: A simple directed graph with integer edge weights from −103 to 103 and n≤103 vertices in the edge list format.

Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). If i is not reachable from 1 set D[i] to x.
'''
filename = 'rosalind_bf.txt'

def bellman_ford(n_vertices, edges):
	dist = [0] + [float('inf')] * (n_vertices-1)
	for _ in range(n_vertices - 1):
		updated = False
		for edge in edges:
			if dist[edge[1]-1] > dist[edge[0]-1] + edge[2]:
				dist[edge[1]-1] = dist[edge[0]-1] + edge[2]
				updated = True
		if not updated:
			break
	return [i if i != float('inf') else 'x' for i in dist]

def main():
	with open(filename) as f:
		n_vertices = int(f.readline().strip().split()[0])
		edges = [[int(i) for i in line.strip().split()] for line in f.readlines()]
	print(' '.join(str(i) for i in bellman_ford(n_vertices, edges)))

if __name__ == '__main__':
	main()
