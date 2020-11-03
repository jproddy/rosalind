'''
Longest Increasing Subsequence
http://rosalind.info/problems/lgis/

Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
'''
import math

filename = 'rosalind_lgis.txt'

def bin_search(seq, i, m, l):
	lo, hi = 1, l
	while lo <= hi:
		mid = math.ceil((lo + hi) / 2)
		if seq[m[mid-1]] < seq[i]:
			lo = mid + 1
		else:
			hi = mid - 1
	return lo

def longest_subsequence(seq):
	# https://en.wikipedia.org/wiki/Longest_increasing_subsequence
	lseq = len(seq)
	p, m = [0] * lseq, [0] * (lseq + 1)
	l = 0
	for i in range(lseq):
		newl = bin_search(seq, i, m, l)
		p[i] = m[newl-2]
		m[newl-1] = i
		l = max(l, newl)

	s = []
	k = m[l-1]
	for _ in range(l):
		s.append(seq[k])
		k = p[k]
	return list(reversed(s))

def main():
	with open(filename) as f:
		f.readline() # discard--len(seq)
		seq = [int(i) for i in f.readline().strip().split()]
	print(' '.join([str(i) for i in longest_subsequence(seq)]))
	print(' '.join([str(i) for i in reversed(longest_subsequence(list(reversed(seq))))]))

if __name__ == '__main__':
	main()
