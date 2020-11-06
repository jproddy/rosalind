'''
Matching a Spectrum to a Protein
http://rosalind.info/problems/prsm/

Given: A positive integer n followed by a collection of n protein strings s1, s2, ..., sn and a multiset R of positive numbers (corresponding to the complete spectrum of some unknown protein string).

Return: The maximum multiplicity of R⊖S[sk] taken over all strings sk, followed by the string sk for which this maximum multiplicity occurs (you may output any such value if multiple solutions exist).
'''
from utils.monoisotopic_mass_table import mmt
from conv import max_mult_spec_conv_shift

filename = 'rosalind_prsm.txt'

def match_protein_spectrum(S, R):
	max_mult, max_string = 0, ''
	for s in S:
		s_spec = [0.0]
		for aa in s:
			s_spec.append(mmt[aa] + s_spec[-1])
		mult, _ = max_mult_spec_conv_shift(s_spec, R)
		if mult > max_mult:
			max_mult = mult
			max_string = s
	return max_mult, max_string

def main():
	with open(filename) as f:
		lines = [line.strip() for line in f.readlines()]
	n = int(lines[0])
	S = lines[1:n+1]
	R = list(map(float, lines[n+1:]))
	print(*match_protein_spectrum(S, R), sep='\n')

if __name__ == '__main__':
	main()
