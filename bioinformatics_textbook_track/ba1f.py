'''
Find a Position in a Genome Minimizing the Skew
http://rosalind.info/problems/ba1f/

Given: A DNA string Genome.

Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).
'''
filename = 'rosalind_ba1f.txt'

def min_skew_indices(genome):
	min_skew, curr_skew, min_indices = 0, 0, []
	for i, base in enumerate(genome):
		if base == 'C':
			curr_skew -= 1
		elif base == 'G':
			curr_skew += 1
		if curr_skew < min_skew:
			min_skew = curr_skew
			min_indices = [i+1]
		elif curr_skew == min_skew:
			min_indices.append(i+1)
	return min_indices

def main():
	with open(filename) as f:
		genome = f.readline().strip()
	print(' '.join(list(map(str, min_skew_indices(genome)))))

if __name__ == '__main__':
	main()
