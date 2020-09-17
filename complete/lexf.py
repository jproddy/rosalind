'''
Enumerating k-mers Lexicographically
http://rosalind.info/problems/lexf/

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).
'''
filename = 'rosalind_lexf.txt'

def lex_kmers(alphabet, n):
	strings = []

	def helper(curr):
		if len(curr) == n:
			strings.append(curr)
		else:
			for char in alphabet:
				helper(curr + char)

	helper('')		
	return strings

def main():
	with open(filename) as f:
		alphabet = f.readline().strip().split()
		n = int(f.readline().strip())
	print('\n'.join(lex_kmers(alphabet, n)))

if __name__ == '__main__':
	main()
