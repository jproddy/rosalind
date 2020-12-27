'''
Distances in Trees
http://rosalind.info/problems/nwck/

Given: A collection of n trees (n≤40) in Newick format, with each tree containing at most 200 nodes; each tree Tk is followed by a pair of nodes xk and yk in Tk.

Return: A collection of n positive integers, for which the kth integer represents the distance between xk and yk in Tk.
'''
from utils.newick import NewickParser

filename = 'rosalind_nwck.txt'

def newick_distance(tree, x, y):
	xpath = find_path(tree, x, [])
	ypath = find_path(tree, y, [])
	i = 0
	while i < len(xpath) and i < len(ypath) and xpath[i] is ypath[i]:
		i += 1
	return len(xpath) + len(ypath) - (2 * i)

def find_path(curr_node, wanted_node, path):
	path.append(curr_node)
	if curr_node.name == wanted_node:
		return path
	elif not curr_node.children:
		path.pop()
		return []
	for child in curr_node.children:
		if find_path(child, wanted_node, path):
			return path
	path.pop()
	return []

def main():
	with open(filename) as f:
		lines = [line.strip() for line in f.readlines()]
	while not lines[-1]:
		lines.pop()

	distances = []
	parser = NewickParser()
	for i in range(len(lines) // 3 + 1):
		tree = parser.parse(lines[3*i])
		x, y = lines[3*i+1].split()
		distances.append(newick_distance(tree, x, y))

	print(*distances)

if __name__ == '__main__':
	main()
