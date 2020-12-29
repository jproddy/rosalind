'''
Compute the Probability of a String Emitted by an HMM
http://rosalind.info/problems/ba10d/

Given: A string x, followed by the alphabet Σ from which x was constructed, followed by the states States, transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).

Return: The probability Pr(x) that the HMM emits x.
'''
import numpy as np

filename = 'rosalind_ba10d.txt'

def emission_probability(x, sigma, states, transition, emission):
	sigma_map = {val: i for i, val in enumerate(sigma)}
	state = emission[:, [sigma_map[x[0]]]] / len(states)

	for i in x[1:]:
		state = (transition * state).sum(axis=0).reshape((-1,1)) * emission[:, [sigma_map[i]]]
	
	return state.sum()

def main():
	with open(filename) as f:
		lines = [line.strip() for line in f.readlines()]
	x = lines[0]
	sigma = lines[2].split()
	states = lines[4].split()
	transition = np.array([list(map(float, line.split()[1:])) for line in lines[7:7+len(states)]])
	emission = np.array([list(map(float, line.split()[1:])) for line in lines[9+len(states):]])
	print(emission_probability(x, sigma, states, transition, emission))

if __name__ == '__main__':
	main()
