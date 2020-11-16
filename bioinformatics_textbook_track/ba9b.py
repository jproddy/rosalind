'''
Implement TrieMatching 
http://rosalind.info/problems/ba9b/

Given: A string Text and a collection of strings Patterns.

Return: All starting positions in Text where a string from Patterns appears as a substring.
'''
from ba9a import create_trie

filename = 'rosalind_ba9b.txt'

def trie_matching(text, trie):
	# a slight deviation from the provided pseudocode
	# but this makes more sense (at least to me)
	v = trie
	for i, symbol in enumerate(text):
		nxt = getattr(v, symbol)
		if nxt:
			i += 1
			v = nxt
		elif not any([v.A, v.C, v.G, v.T]):
			return i
		else:
			return 0
	return i if not any([v.A, v.C, v.G, v.T]) else 0

def prefix_trie_matching(text, trie):
	results = []
	for i in range(len(text)):
		val = trie_matching(text[i:], trie)
		if val:
			results.append(i)
	return results

def main():
	with open(filename) as f:
		text = f.readline().strip()
		patterns = [line.strip() for line in f.readlines()]
	trie = create_trie(patterns)
	print(*prefix_trie_matching(text, trie))

if __name__ == '__main__':
	main()
