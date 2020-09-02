class Node:
	def __init__(self, value):
		self.value = value
		self.A = None
		self.C = None
		self.T = None
		self.G = None

def parse_file():
	with open('rosalind_trie.txt') as f:
		lines = f.readlines()
	words = [line.strip() for line in lines]
	return words


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
	words = parse_file()
	trie = create_trie(words)
	print_trie(trie)



if __name__ == '__main__':
	main()