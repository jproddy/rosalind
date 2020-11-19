'''
Compute the Probability of an Outcome Given a Hidden Path
http://rosalind.info/problems/ba10b/

Given: A string x, followed by the alphabet Σ from which x was constructed, followed by a hidden path π, followed by the states States and emission matrix Emission of an HMM (Σ, States, Transition, Emission).

Return: The conditional probability Pr(x|π) that string x will be emitted by the HMM given the hidden path π.
'''
import pandas as pd

filename = 'rosalind_ba10b.txt'

def prob_emitted_hmm(x, pi, emission):
	probability = 1
	for i in range(len(x)):
		probability *= emission.loc[pi[i], x[i]]
	return probability

def main():
	with open(filename) as f:
		x = f.readline().strip()
		f.readline()
		f.readline()
		f.readline()
		pi = f.readline().strip()
		f.readline()
		f.readline()
		f.readline()
		cols = f.readline().split()
		index, data = [], []
		for line in f.readlines():
			row = line.split()
			index.append(row[0])
			data.append(list(map(float, row[1:])))
		emission = pd.DataFrame(data, index=index, columns=cols)

	print(prob_emitted_hmm(x, pi, emission))

if __name__ == '__main__':
	main()
