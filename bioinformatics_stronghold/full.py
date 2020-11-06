'''
Inferring Peptide from Full Spectrum
http://rosalind.info/problems/full/

Given: A list L containing 2n+3 positive real numbers (n≤100). The first number in L is the parent mass of a peptide P, and all other numbers represent the masses of some b-ions and y-ions of P (in no particular order). You may assume that if the mass of a b-ion is present, then so is that of its complementary y-ion, and vice-versa.

Return: A protein string t of length n for which there exist two positive real numbers w1 and w2 such that for every prefix p and suffix s of t, each of w(p)+w1 and w(s)+w2 is equal to an element of L. (In other words, there exists a protein string whose t-prefix and t-suffix weights correspond to the non-parent mass values of L.) If multiple solutions exist, you may output any one.
'''
from utils.monoisotopic_mass_table import inverted_mmt

filename = 'rosalind_full.txt'
ROUND = 5

def infer_protein(peptide_mass, L):
	# greedy algorithm--could potentially provide an incorrect answer
	# if nxt-cur equals the mass of an amino acid, but one of nxt or cur
	# is a t-prefix and the other is a t-suffix
	cur = L[0]
	peptide = ''
	ignore = {len(L) - 1}
	for i, nxt in enumerate(L[1:]):
		val = round(nxt - cur, ROUND)
		if val in inverted_mmt and i not in ignore:
			peptide += inverted_mmt[val]
			cur = nxt
			ignore.add(len(L)-2)
	return peptide

def main():
	with open(filename) as f:
		peptide_mass = f.readline()
		L = [float(line.strip()) for line in f.readlines()]
	print(infer_protein(peptide_mass, L))

if __name__ == '__main__':
	main()
