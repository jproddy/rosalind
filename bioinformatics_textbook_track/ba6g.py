'''
Implement CycleToChromosome
http://rosalind.info/problems/ba6g/

Given: A sequence Nodes of integers between 1 and 2n.

Return: The chromosome Chromosome containing n synteny blocks resulting from applying CycleToChromosome to Nodes.
'''
filename = 'rosalind_ba6g.txt'

def cycle_to_chromosome(nodes):
	chromosome = [0] * (len(nodes) // 2)
	for j in range(len(nodes) // 2):
		if nodes[2*j] < nodes[2*j+1]:
			chromosome[j] = nodes[2*j+1] // 2
		else:
			chromosome[j] = -nodes[2*j] // 2
	return chromosome

def main():
	with open(filename) as f:
		nodes = list(map(int, f.readline().strip()[1:-1].split()))
	s = ' '.join(str(i) if i < 0 else '+' + str(i) for i in cycle_to_chromosome(nodes))
	print(f'({s})')

if __name__ == '__main__':
	main()
