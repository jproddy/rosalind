'''
Transitions and Transversions
http://rosalind.info/problems/tran/

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).
'''
from utils.parse_fasta import parse_fasta_as_list

filename = 'rosalind_tran.txt'

def transition_transversion_ratio(s1, s2):
	purines = ['A', 'G']
	pyrimidines = ['T', 'C']
	transitions = []
	for i, j in zip(s1, s2):
		if i != j:
			# ignores matches, appends True if transition, False if transversion
			transitions.append((i in purines and j in purines) or (i in pyrimidines and j in pyrimidines))
	return sum(transitions) / (len(transitions) - sum(transitions))

def main():
	with open(filename) as f:
		fasta = f.read()
	s1, s2 = parse_fasta_as_list(fasta)
	print(transition_transversion_ratio(s1, s2))

if __name__ == '__main__':
	main()
