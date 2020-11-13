'''
Construct the Overlap Graph of a Collection of k-mers
http://rosalind.info/problems/ba3c/

Given: A collection Patterns of k-mers.

Return: The overlap graph Overlap(Patterns), in the form of an adjacency list.
'''
filename = 'rosalind_ba3c.txt'

def overlap(patterns):
	# space-expensive but linear runtime
	prefixes = {pattern: pattern[1:] for pattern in patterns}
	suffixes = {pattern[:-1]: pattern for pattern in patterns}
	return {pattern: suffixes[overlap] for pattern, overlap in prefixes.items() if overlap in suffixes}

def main():
	with open(filename) as f:
		patterns = [line.strip() for line in f.readlines()]
	for k, v in overlap(patterns).items():
		print(f'{k} -> {v}')

if __name__ == '__main__':
	main()
