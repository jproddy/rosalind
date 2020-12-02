'''
Implement ChromosomeToCycle
http://rosalind.info/problems/ba6f/

Given: A chromosome Chromosome containing n synteny blocks.

Return: The sequence Nodes of integers between 1 and 2n resulting from applying ChromosomeToCycle to Chromosome.
'''
filename = 'rosalind_ba6f.txt'

def chromosome_to_cycle(chromosome):
	nodes = [0] * (len(chromosome) * 2)
	for j in range(len(chromosome)):
		i = chromosome[j]
		if i > 0:
			nodes[2*j] = 2 * i - 1
			nodes[2*j+1] = 2 * i
		else:
			nodes[2*j] = -2 * i
			nodes[2*j+1] = -2 * i - 1
	return nodes

def main():
	with open(filename) as f:
		chromosome = list(map(int, f.readline().strip()[1:-1].split()))
	s = ' '.join(str(i) for i in chromosome_to_cycle(chromosome))
	print(f'({s})')

if __name__ == '__main__':
	main()
