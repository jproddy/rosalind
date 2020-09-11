def add_s(alphabet, n, words, s):
	words.append(s)
	if len(s) != n:
		for letter in alphabet:
			add_s(alphabet, n, words, s+letter)



def main():
	alphabet = 'M R L P V O U B N C Y Q'
	n = 4
	alphabet = alphabet.split()
	words = []
	add_s(alphabet, n, words, '')

	for word in words[1:]:
		print(word)

	print(len(words) - 1)




if __name__ == '__main__':
	main()
