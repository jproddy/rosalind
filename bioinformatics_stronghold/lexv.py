'''
Ordering Strings of Varying Length Lexicographically
http://rosalind.info/problems/lexv/

Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).

Return: All strings of length at most n formed from A, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)
'''
filename = 'rosalind_lexv.txt'

def generate_strings(alphabet, n):
	strings = []
	def add_s(s=''):
		strings.append(s)
		if len(s) != n:
			for letter in alphabet:
				add_s(s + letter)
	add_s()
	return strings[1:] # exclude the initial empty string

def main():
	with open(filename) as f:
		alphabet = f.readline().strip().split()
		n = int(f.readline().strip())
	alphabet = ['D','N','A']
	n=3
	print('\n'.join(generate_strings(alphabet, n)))

if __name__ == '__main__':
	main()
