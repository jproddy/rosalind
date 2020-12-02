'''
Find All Shared k-mers of a Pair of Strings
http://rosalind.info/problems/ba6e/

Given: An integer k and two strings.

Return: All k-mers shared by these strings, in the form of ordered pairs (x, y) corresponding to starting positions of these k-mers in the respective strings.
'''
from ba1c import reverse_complement

filename = 'rosalind_ba6e.txt'

def shared_kmers(k, s1, s2):
	d1, d2 = {}, {}
	for i in range(len(s1) - k + 1):
		ss = s1[i:i+k]
		ss_revc = reverse_complement(ss)
		if ss in d1:
			d1[ss].append(i)
		else:
			d1[ss] = [i]
		if ss_revc in d1:
			d1[ss_revc].append(i)
		else:
			d1[ss_revc] = [i]
	for i in range(len(s2) - k + 1):
		ss = s2[i:i+k]
		if ss in d2:
			d2[ss].append(i)
		else:
			d2[ss] = [i]

	kmer_locs = []
	for key in d1:
		if key in d2:
			kmer_locs.extend([(i, j) for i in d1[key] for j in d2[key]])

	return kmer_locs

def main():
	with open(filename) as f:
		k = int(f.readline().strip())
		s1 = f.readline().strip()
		s2 = f.readline().strip()
	print(*shared_kmers(k, s1, s2), sep='\n')

if __name__ == '__main__':
	main()
