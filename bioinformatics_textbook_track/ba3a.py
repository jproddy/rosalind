'''
Generate the k-mer Composition of a String
http://rosalind.info/problems/ba3a/

Given: An integer k and a string Text.

Return: Compositionk(Text) (the k-mers can be provided in any order).
'''
filename = 'rosalind_ba3a.txt'

def kmer_composition(k, text):
	kmers = set([text[i:i+k] for i in range(len(text)- k + 1)])
	return sorted(kmers)

def main():
	with open(filename) as f:
		k = int(f.readline().strip())
		text = f.readline().strip()
	for kmer in kmer_composition(k, text):
		print(kmer)

if __name__ == '__main__':
	main()
