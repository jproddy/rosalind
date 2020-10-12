'''
Dictionaries
http://rosalind.info/problems/ini6/

Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
'''
from collections import Counter

filename = 'rosalind_ini6.txt'

def word_counter(words):
	return Counter(words)

def main():
	with open(filename) as f:
		words = f.readline().strip().split()
	for k, v in word_counter(words).items():
		print(k, v)

if __name__ == '__main__':
	main()
