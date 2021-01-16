'''
Compute Distances Between Leaves
http://rosalind.info/problems/ba7a/

Given: An integer n followed by the adjacency list of a weighted tree with n leaves.

Return: A space-separated n x n (di, j), where di, j is the length of the path between leaves i and j.
'''
import numpy as np

filename = 'rosalind_ba7a.txt'

def leaf_distances(n, adj):
	arr = np.zeros((n, n), dtype=int)
	
	def dfs(curr_node, start_node, to_find, curr_dist, seen):
		seen.add(curr_node)
		for next_node, next_dist in adj[curr_node].items():
			if not to_find:
				return
			elif next_node in to_find:
				arr[start_node, next_node] = arr[next_node, start_node] = curr_dist + next_dist
				to_find.remove(next_node) # dont need to add to seen--impossible to reach again
			elif next_node not in seen:
				dfs(next_node, start_node, to_find, curr_dist + next_dist, seen)

	for i in range(n - 1):
		to_find = {j for j in range(i+1, n)}
		dfs(i, i, to_find, 0, set())

	return arr

def main():
	with open(filename) as f:
		n = int(f.readline().strip())
		lines = [line.strip() for line in f.readlines()]
	adj = {}
	for line in lines:
		l = line.split('->')
		start = int(l[0])
		l = l[1].split(':')
		end = int(l[0])
		weight = int(l[1])
		if start in adj:
			adj[start][end] = weight
		else:
			adj[start] = {end: weight}
	arr = leaf_distances(n, adj)
	for row in arr:
		print(*row)

if __name__ == '__main__':
	main()
