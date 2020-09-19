'''
Introduction to Pattern Matching
http://rosalind.info/problems/trie/

Given: A list of at most 100 DNA strings of length at most 100 bp, none of which is a prefix of another.

Return: The adjacency list corresponding to the trie T for these patterns, in the following format. If T has n nodes, first label the root with 1 and then label the remaining nodes with the integers 2 through n in any order you like. Each edge of the adjacency list of T will be encoded by a triple containing the integer representing the edge's parent node, followed by the integer representing the edge's child node, and finally the symbol labeling the edge.
'''
filename = 'rosalind_trie.txt'

class Node:
	def __init__(self, value):
		self.value = value
		self.A = None
		self.C = None
		self.T = None
		self.G = None

def create_trie(words):
	head = Node(1)
	counter = 2
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
			print(node.value, getattr(node, base).value, base)
			print_trie(getattr(node, base))

def main():
	with open(filename) as f:
		lines = f.readlines()
	words = [line.strip() for line in lines]
	trie = create_trie(words)
	print_trie(trie)

if __name__ == '__main__':
	main()
