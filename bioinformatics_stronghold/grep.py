'''
Genome Assembly with Perfect Coverage and Repeats
http://rosalind.info/problems/grep/

Given: A list Sk+1 of error-free DNA (k+1)-mers (k≤5) taken from the same strand of a circular chromosome (of length ≤50).

Return: All circular strings assembled by complete cycles in the de Bruijn graph Bk of Sk+1. The strings may be given in any order, but each one should begin with the first (k+1)-mer provided in the input.
'''
import copy

filename = 'rosalind_grep.txt'

def assemble_genome(dnas):
	adj_start = {}
	str_start = dnas[0]
	k = len(str_start) # len kmer
	expected_len = len(dnas) # number of kmers = expected len of cycle
	for dna in dnas[1:]:
		if dna[:-1] in adj_start:
			adj_start[dna[:-1]].append(dna[1:])
		else:
			adj_start[dna[:-1]] = [dna[1:]]
	cycles = set()

	# depth-first traversal?
	def dfs(curr_str, curr_adj):
		next_node = curr_adj[curr_str[-k+1:]]
		next_node_set = set(next_node)
		if len(next_node) == 0 and len(curr_str) == expected_len + k - 1:
			# first condition checks for the end of a cycle
			# second condition ensures that the cycle is eulerian
			# trim the last k-1 elements because they are wraparound
				cycles.add(curr_str[:-k+1])
		elif len(next_node_set) == 1:
			edge = next_node.pop()
			dfs(curr_str + edge[-1], curr_adj)
		else:
			for edge in next_node_set:
				next_node.remove(edge)
				dfs(curr_str + edge[-1], copy.deepcopy(curr_adj))
				next_node.append(edge)

	dfs(str_start, adj_start)
	return cycles

def main():
	with open(filename) as f:
		lines = [line.strip() for line in f.readlines()]
	print(*assemble_genome(lines), sep='\n')

if __name__ == '__main__':
	main()
