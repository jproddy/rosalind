'''
Connected Components
https://www.youtube.com/watch?v=j-msPq4XX_4

Given: A simple graph with n≤103 vertices in the edge list format.

Return: The number of connected components in the graph.
'''
from ddeg import adjacency_list

filename = 'rosalind_cc.txt'

def find_connected_components(edges, n):
	adj_list = adjacency_list(edges, n)
	found_connection = set()
	count = 0
	def dfs(i):
		if i not in found_connection:
			found_connection.add(i)
			for vertex in adj_list[i]:
				dfs(vertex)
	for i in range(1, n+1):
		if i not in found_connection:
			dfs(i)
			count += 1
	return count

def main():
	with open(filename) as f:
		n = int(f.readline().strip().split()[0])
		edges = [[int(i) for i in line.strip().split()] for line in f.readlines()]
	print(find_connected_components(edges, n))

if __name__ == '__main__':
	main()
