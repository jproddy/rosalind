'''
Find the Most Frequent Words in a String
http://rosalind.info/problems/ba1b/

Given: A DNA string Text and an integer k.

Return: All most frequent k-mers in Text (in any order).
'''
from collections import Counter

filename = 'rosalind_ba1b.txt'

def most_freq_kmer(text, k):
	c = Counter([text[i:i+k] for i in range(len(text)-k+1)])
	highest_count = max(c.values())
	return [k for k in c if c[k] == highest_count]

def main():
	with open(filename) as f:
		text = f.readline().strip()
		k = int(f.readline().strip())
	print(*most_freq_kmer(text, k))

if __name__ == '__main__':
	main()
