'''
Trim a Peptide Leaderboard
http://rosalind.info/problems/ba4l/

Given: A leaderboard of linear peptides Leaderboard, a linear spectrum Spectrum, and an integer N.

Return: The top N peptides from Leaderboard scored against Spectrum. Remember to use LinearScore.
'''
from utils.monoisotopic_mass_table import int_mmt
from ba4k import linear_score

filename = 'rosalind_ba4l.txt'

def trim(leaderboard, spectrum, N):
	scores = {peptide: linear_score(peptide, spectrum) for peptide in leaderboard}
	sorted_scores = sorted(scores, key=lambda x: scores[x], reverse=True)
	return sorted_scores[:N]

def main():
	with open(filename) as f:
		leaderboard = f.readline().strip().split()
		spectrum = list(map(int, f.readline().strip().split()))
		N = int(f.readline().strip())
	print(*trim(leaderboard, spectrum, N))

if __name__ == '__main__':
	main()
