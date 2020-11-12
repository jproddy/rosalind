'''
Generate the d-Neighborhood of a String
http://rosalind.info/problems/ba1n/

Given: A DNA string Pattern and an integer d.

Return: The collection of strings Neighbors(Pattern, d).
'''
filename = 'rosalind_ba1n.txt'
BASES = ['A', 'C', 'G', 'T']

def neighbors(pattern, d):
	if d == 0:
		return [pattern]
	elif len(pattern) == 1:
		return BASES

	neighborhood = []
	subsequent_neighbors = neighbors(pattern[1:], d-1)

	for base in BASES:
		if base == pattern[0]:
			neighborhood.extend([base + n for n in neighbors(pattern[1:], d)])
		else:
			neighborhood.extend([base + sn for sn in subsequent_neighbors])

	return neighborhood

def main():
	with open(filename) as f:
		pattern = f.readline().strip()
		d = int(f.readline().strip())
	for i in neighbors(pattern, d):
		print(i)

if __name__ == '__main__':
	main()
