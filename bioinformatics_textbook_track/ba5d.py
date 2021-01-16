'''
Find the Longest Path in a DAG
http://rosalind.info/problems/ba5d/
Given: An integer representing the source node of a graph, followed by an integer representing the sink node of the graph, followed by an edge-weighted graph. The graph is represented by a modified adjacency list in which the notation "0->1:7" indicates that an edge connects node 0 to node 1 with weight 7.

Return: The length of a longest path in the graph, followed by a longest path. (If multiple longest paths exist, you may return any one.)
'''
filename = 'rosalind_ba5d.txt'

def longest_path(source, sink, adj):
	longest_dist = 0
	longest_path = []
	
	def dfs(curr_node, curr_dist, curr_path):
		nonlocal longest_dist, longest_path # is this bad form? hopefully not...
		for next_node, next_dist in adj[curr_node].items():
			if next_node == sink:
				if curr_dist + next_dist > longest_dist:
					longest_dist = curr_dist + next_dist
					longest_path = curr_path + [next_node]
			elif next_node in adj:
				dfs(next_node, curr_dist + next_dist, curr_path.copy() + [next_node])

	dfs(source, 0, [source])
	return longest_dist, longest_path

def main():
	with open(filename) as f:
		source = int(f.readline().strip())
		sink = int(f.readline().strip())
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
	longest = longest_path(source, sink, adj)
	print(longest[0])
	print('->'.join(map(str, longest[1])))

if __name__ == '__main__':
	main()
