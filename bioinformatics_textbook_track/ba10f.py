'''
Construct a Profile HMM with Pseudocounts
http://rosalind.info/problems/ba10f/

Given: A threshold θ and a pseudocount σ, followed by an alphabet Σ, followed by a multiple alignment Alignment whose strings are formed from Σ.

Return: The transition and emission probabilities of the profile HMM HMM(Alignment, θ, σ).
'''
import numpy as np

from ba10e import profile_hmm

filename = 'rosalind_ba10f.txt'

def profile_hmm_pseudocounts(theta, pseudocount, sigma, alignment): 
	transition, emission, state_index = profile_hmm(theta, sigma, alignment)

	# modify emission with pseudocounts
	for i, s in enumerate(state_index):
		if s[0] in ('I', 'M'):
			if emission[i, :].sum() == 0:
				emission[i, :] = 1 / len(sigma)
			else:
				emission[i, :] *= 1 - (pseudocount * len(sigma))
				emission[i, :] += pseudocount

	# modify transition with pseudocounts
	for i in range(transition.shape[0] - 1):
		# start col to manage offset due to matrix asymmetry
		start_col = ((i + 1) // 3) * 3 + 1
		end_col = start_col + 3
		if transition.shape[0] - 2 >= i >= transition.shape[0] - 4:
			end_col -= 1

		if transition[i, start_col:end_col].sum() == 0:
			transition[i, start_col:end_col] = 1 / (end_col - start_col)
		else:
			transition[i, start_col:end_col] *= 1 - (pseudocount * (end_col - start_col))
			transition[i, start_col:end_col] += pseudocount

	return transition, emission, state_index

def main():
	with open(filename) as f:
		lines = [line.strip() for line in f.readlines()]
	theta, pseudocount = list(map(float, lines[0].split()))
	sigma = lines[2].split()
	alignment = np.array([list(s) for s in lines[4:]])

	transition, emission, state_index = profile_hmm_pseudocounts(theta, pseudocount, sigma, alignment)

	print('', *state_index, sep='\t')
	for i, row in zip(state_index, transition):
		print(i, *row, sep='\t')
	print('--------')
	print('', *sigma, sep='\t')
	for i, row in zip(state_index, emission):
		print(i, *row, sep='\t')

if __name__ == '__main__':
	main()
