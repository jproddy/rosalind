'''
Compute the Number of Times a Pattern Appears in a Text
http://rosalind.info/problems/ba1a/

Given: {DNA strings}} Text and Pattern.

Return: Count(Text, Pattern).
'''
filename = 'rosalind_ba1a.txt'

def count(text, pattern):
	len_t, len_p = len(text), len(pattern)
	counter = 0
	for i in range(len_t - len_p + 1):
		if text[i:i+len_p] == pattern:
			counter += 1
	return counter

def main():
	with open(filename) as f:
		text = f.readline().strip()
		pattern = f.readline().strip()
	print(count(text, pattern))

if __name__ == '__main__':
	main()
