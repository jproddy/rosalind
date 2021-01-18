'''
Creating a Character Table
http://rosalind.info/problems/ctbl/

Given: An unrooted binary tree T in Newick format for at most 200 species taxa.

Return: A character table having the same splits as the edge splits of T. The columns of the character table should encode the taxa ordered lexicographically; the rows of the character table may be given in any order. Also, for any given character, the particular subset of taxa to which 1s are assigned is arbitrary.
'''
from utils.newick import NewickParser

filename = 'rosalind_ctbl.txt'

def character_table(tree):
	splits = []
	# use dfs to populate each node.value with all leaves within its subtree
	# also fills splits with valid sets when it sees them
	dfs_leaves(tree, splits)
	leaves = tree.value
	s_leaves = sorted(leaves)
	n_leaves = len(leaves)
	return [''.join([str(int(leaf in split)) for leaf in s_leaves]) for split in splits if len(split) < (n_leaves - 1)]

def dfs_leaves(root, splits):
	root.value = set()
	for child in root.children:
		if child.name:
			child.value = {child.name}
		else:
			dfs_leaves(child, splits)
		root.value |= child.value
	if len(root.value) > 1:
		splits.append(root.value)

def main():
	with open(filename) as f:
		tree = f.readline().strip()
	c_table = character_table(NewickParser().parse(tree))
	print(*c_table, sep='\n')

if __name__ == '__main__':
	main()
