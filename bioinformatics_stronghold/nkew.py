'''
Newick Format with Edge Weights
http://rosalind.info/problems/nkew/

Given: A collection of n weighted trees (n≤40) in Newick format, with each tree containing at most 200 nodes; each tree Tk is followed by a pair of nodes xk and yk in Tk.

Return: A collection of n numbers, for which the kth number represents the distance between xk and yk in Tk.
'''
from utils.newick import NewickParser
from nwck import find_path

filename = 'rosalind_nkew.txt'

def newick_distance_edge_weights(tree, x, y):
	xpath = find_path(tree, x, [])
	ypath = find_path(tree, y, [])
	i = 0
	while i < len(xpath) and i < len(ypath) and xpath[i] is ypath[i]:
		i += 1
	distance = sum(node.value for node in xpath[i:]) + sum(node.value for node in ypath[i:])
	if distance.is_integer():
		return int(distance)
	else:
		return distance

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
		distances.append(newick_distance_edge_weights(tree, x, y))

	print(*distances)

if __name__ == '__main__':
	main()
