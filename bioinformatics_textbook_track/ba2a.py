'''
Implement MotifEnumeration
http://rosalind.info/problems/ba2a/

Given: Integers k and d, followed by a collection of strings Dna.

Return: All (k, d)-motifs in Dna.
'''
from ba1n import neighbors

filename = 'rosalind_ba2a.txt'

def motif_enumeration(dnas, k, d):
	# deviates from the given algorithm, but this made a lot more sense to me
	patterns = kd_motifs_in_strand(dnas[0], k, d)
	for dna in dnas[1:]:
		patterns = set.intersection(patterns, kd_motifs_in_strand(dna, k, d))
	return patterns

def kd_motifs_in_strand(dna, k, d):
	motifs = set()
	for i in range(len(dna) - k + 1):
		substring = dna[i:i+k]
		motifs.update(neighbors(substring, d))
	return motifs

def main():
	with open(filename) as f:
		k, d = list(map(int, f.readline().strip().split()))
		dnas = [line.strip() for line in f.readlines()]
	print(*motif_enumeration(dnas, k, d))

if __name__ == '__main__':
	main()
