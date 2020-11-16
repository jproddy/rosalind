'''
Construct a Trie from a Collection of Patterns
http://rosalind.info/problems/ba9a/

Given: A collection of strings Patterns.

Return: The adjacency list corresponding to Trie(Patterns), in the following format. If Trie(Patterns) has n nodes, first label the root with 1 and then label the remaining nodes with the integers 2 through n in any order you like. Each edge of the adjacency list of Trie(Patterns) will be encoded by a triple: the first two members of the triple must be the integers labeling the initial and terminal nodes of the edge, respectively; the third member of the triple must be the symbol labeling the edge.
'''
# code from bioinformatics_stronghold/trie
# but start at 0 instead of 1--description is incorrect
# and change print_trie to fit new format
filename = 'rosalind_ba9a.txt'

class Node:
	def __init__(self, value):
		self.value = value
		self.A = None
		self.C = None
		self.T = None
		self.G = None

def create_trie(words):
	head = Node(0)
	counter = 1
	for word in words:
		curr = head
		for base in word:
			if getattr(curr, base):
				curr = getattr(curr, base)
			else:
				setattr(curr, base, Node(counter))
				curr = getattr(curr, base)
				counter += 1
	return head

def print_trie(node):
	bases = ['A', 'C', 'G', 'T']
	for base in bases:
		if getattr(node, base):
			print(f'{node.value}->{getattr(node, base).value}:{base}')
			print_trie(getattr(node, base))

def main():
	with open(filename) as f:
		lines = f.readlines()
	words = [line.strip() for line in lines]
	trie = create_trie(words)
	print_trie(trie)

if __name__ == '__main__':
	main()
