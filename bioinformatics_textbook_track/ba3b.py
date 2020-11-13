'''
Reconstruct a String from its Genome Path
http://rosalind.info/problems/ba3b/

Given: A sequence of k-mers Pattern1, ... , Patternn such that the last k - 1 symbols of Patterni are equal to the first k - 1 symbols of Patterni+1 for i from 1 to n-1.

Return: A string Text of length k+n-1 where the i-th k-mer in Text is equal to Patterni for all i.
'''
filename = 'rosalind_ba3b.txt'

def reconstruct(patterns):
	return ''.join([pattern[0] for pattern in patterns[:-1]]) + patterns[-1]

def main():
	with open(filename) as f:
		patterns = [line.strip() for line in f.readlines()]
	print(reconstruct(patterns))

if __name__ == '__main__':
	main()
