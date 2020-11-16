'''
Construct the De Bruijn Graph of a Collection of k-mers
http://rosalind.info/problems/ba3e/

Given: A collection of k-mers Patterns.

Return: The de Bruijn graph DeBruijn(Patterns), in the form of an adjacency list.
'''
filename = 'rosalind_ba3e.txt'

def de_brujin(patterns):
	adj_list = {}
	for pattern in patterns:
		prefix = pattern[:-1]
		suffix = pattern[1:]
		if prefix in adj_list:
			adj_list[prefix].append(suffix)
		else:
			adj_list[prefix] = [suffix]
	return adj_list

def main():
	with open(filename) as f:
		patterns = [line.strip() for line in f.readlines()]
	for key, val in de_brujin(patterns).items():
		v = ','.join(val)
		print(f'{key} -> {v}')

if __name__ == '__main__':
	main()
