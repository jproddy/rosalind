'''
Implement GreedyMotifSearch
http://rosalind.info/problems/ba2d/

Given: Integers k and t, followed by a collection of strings Dna.

Return: A collection of strings BestMotifs resulting from running GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.
'''
import pandas as pd

from ba1g import hamming_distance
from ba2c import profile_most_probable

filename = 'rosalind_ba2d.txt'
BASES = ['A', 'C', 'G', 'T']

def greedy_motif_search(dnas, k, t):
	# took ~4 min to run on test dataset but seems to be the correct algorithm
	# based on pseudocode (and other peoples' submissions)
	best_motifs = [dna[:k] for dna in dnas]
	best_score = score_motifs(best_motifs)
	for i in range(len(dnas[0]) - k + 1):
		print(i)
		motifs = [dnas[0][i:i+k]]
		for j in range(1, t):
			motifs.append(profile_most_probable(dnas[j], k, form_profile(motifs)))
		score = score_motifs(motifs)
		if score < best_score:
			best_motifs = motifs
			best_score = score
	return best_motifs

def form_profile(motifs):
	profile = pd.DataFrame(0, columns=range(len(motifs[0])), index=BASES)
	for motif in motifs:
		for i, base in enumerate(motif):
			profile.loc[base, i] += 1
	return profile / len(motifs)

def score_motifs(motifs):
	# couldn't figure out what 'score' from pseudocode meant :(
	# had to reference someone else's code:
	# https://github.com/NathanielLovin/Rosalind/blob/master/BA2D.py
	profile = form_profile(motifs)
	# neat df function generates the consensus string
	consensus = ''.join(profile.idxmax())
	return sum(hamming_distance(motif, consensus) for motif in motifs)

def main():
	with open(filename) as f:
		k, t = list(map(int, f.readline().strip().split()))
		dnas = [line.strip() for line in f.readlines()]
	for motif in greedy_motif_search(dnas, k, t):
		print(motif)

if __name__ == '__main__':
	main()
