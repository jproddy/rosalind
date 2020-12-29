'''
Construct a Profile HMM
http://rosalind.info/problems/ba10e/

Given: A threshold θ, followed by an alphabet Σ, followed by a multiple alignment Alignment whose strings are formed from Σ.

Return: The transition and emission probabilities of the profile HMM HMM(Alignment, θ).
'''
import numpy as np

filename = 'rosalind_ba10e.txt'

def profile_hmm(theta, sigma, alignment):
	# a useful reading:
	# https://www.cs.princeton.edu/~mona/Lecture/HMM1.pdf
	match_states = (alignment == '-').mean(axis=0) < theta
	states = np.empty(alignment.shape, dtype='U2')

	m_i = 0
	for i in range(alignment.shape[1]):
		if match_states[i]:
			m_i += 1
			states[:, i] = np.where(alignment[:, i] != '-', f'M{m_i}', f'D{m_i}')
		else:
			states[:, i] = np.where(alignment[:, i] != '-', f'I{m_i}', '*')

	state_index = ['S', 'I0'] + [f'{s}{i}' for i in range(1, sum(match_states) + 1) for s in ['M', 'D', 'I']] + ['E']
	state_index = {val: i for i, val in enumerate(state_index)}
	sigma_index = {val: i for i, val in enumerate(sigma)}

	emission = np.zeros((len(state_index), len(sigma)))
	transition = np.zeros((len(state_index), len(state_index)))

	# calculate emission
	for i in range(alignment.shape[0]):
		for j in range(alignment.shape[1]):
			state = states[i, j]
			if alignment[i, j] != '-':
				emission[state_index[state], sigma_index[alignment[i, j]]] += 1

	# calcuate transition
	for i in range(alignment.shape[0]):
		transition[state_index['S'], state_index[states[i, 0]]] += 1
		prev, curr = 0, 1
		while curr < alignment.shape[1]:
			if states[i, curr] != '*':
				transition[state_index[states[i, prev]], state_index[states[i, curr]]] += 1
				prev = curr
			curr += 1
		transition[state_index[states[i, prev]], state_index['E']] += 1

	# normalize rows
	normalization_e = emission.sum(axis=1, keepdims=True)
	emission /= np.where(normalization_e, normalization_e, 1)
	normalization_t = transition.sum(axis=1, keepdims=True)
	transition /= np.where(normalization_t, normalization_t, 1)

	return transition, emission, state_index


def main():
	with open(filename) as f:
		lines = [line.strip() for line in f.readlines()]
	theta = float(lines[0])
	sigma = lines[2].split()
	alignment = np.array([list(s) for s in lines[4:]])

	transition, emission, state_index = profile_hmm(theta, sigma, alignment)

	print('', *state_index, sep='\t')
	for i, row in zip(state_index, transition):
		print(i, *row, sep='\t')
	print('--------')
	print('', *sigma, sep='\t')
	for i, row in zip(state_index, emission):
		print(i, *row, sep='\t')


if __name__ == '__main__':
	main()
