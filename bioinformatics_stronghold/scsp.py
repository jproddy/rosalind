'''
Interleaving Two Motifs
http://rosalind.info/problems/scsp/

Given: Two DNA strings s and t.

Return: A shortest common supersequence of s and t. If multiple solutions exist, you may output any one.
'''
import numpy as np

from lcsq import longest_common_subsequence

filename = 'rosalind_scsp.txt'

def shortest_common_supersequence(s, t):
	scs = []
	lcs = longest_common_subsequence(s, t)
	si, ti, lcsi = 0, 0, 0
	while lcsi < len(lcs):
		while s[si] != lcs[lcsi]:
			scs.append(s[si])
			si += 1
		while t[ti] != lcs[lcsi]:
			scs.append(t[ti])
			ti += 1
		scs.append(lcs[lcsi])
		lcsi += 1
		si += 1
		ti += 1
	return ''.join(scs) + t[ti:] + s[si:]

def main():
	with open(filename) as f:
		s = f.readline().strip()
		t = f.readline().strip()
	print(shortest_common_supersequence(s, t))

if __name__ == '__main__':
	main()
