'''
Compute the Probability of a Hidden Path
http://rosalind.info/problems/ba10a/

Given: A hidden path π followed by the states States and transition matrix Transition of an HMM (Σ, States, Transition, Emission).

Return: The probability of this path, Pr(π). You may assume that initial probabilities are equal.
'''
filename = 'rosalind_ba10a.txt'

def p_path(path, states, transition):
	p = 1 / len(states) # initial probability dependant on number of states
	for i in range(len(path)-1):
		p *= transition[path[i:i+2]]
	return p

def main():
	with open(filename) as f:
		path = f.readline().strip()
		f.readline()
		states = f.readline().strip().split()
		f.readline()
		f.readline()
		matrix = [line.strip().split() for line in f.readlines()]
	transition = {}
	for row in matrix:
		for i, prob in enumerate(row[1:]):
			transition[row[0] + states[i]] = float(prob)
	print(p_path(path, states, transition))

if __name__ == '__main__':
	main()
