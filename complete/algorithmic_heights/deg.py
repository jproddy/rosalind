'''
Degree Array
http://rosalind.info/problems/deg/

Given: A simple graph with n≤103 vertices in the edge list format.

Return: An array D[1..n] where D[i] is the degree of vertex i.
'''
filename = 'rosalind_deg.txt'

def degree(edges):
	vertices = {}
	for edge in edges:
		vertices[edge[0]] = vertices.get(edge[0], 0) + 1
		vertices[edge[1]] = vertices.get(edge[1], 0) + 1
	return vertices

def main():
	with open(filename) as f:
		f.readline() # discard the first line
		edges = [[int(i) for i in line.strip().split()] for line in f.readlines()]
		print(edges)
	vertices = degree(edges)
	print(' '.join([str(vertices[i]) for i in range(1, len(vertices)+1)]))

if __name__ == '__main__':
	main()
