'''
Find All Occurrences of a Pattern in a String
http://rosalind.info/problems/ba1d/

Given: Strings Pattern and Genome.

Return: All starting positions in Genome where Pattern appears as a substring. Use 0-based indexing.
'''
filename = 'rosalind_ba1d.txt'

def pattern_indices(pattern, genome):
	# could also just do with regex
	lp = len(pattern)
	return [i for i in range(len(genome) - lp + 1) if genome[i:i+lp] == pattern]

def main():
	with open(filename) as f:
		pattern = f.readline().strip()
		genome = f.readline().strip()
	print(pattern, genome)
	print(' '.join(list(map(str, pattern_indices(pattern, genome)))))

if __name__ == '__main__':
	main()
