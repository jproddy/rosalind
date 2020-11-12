'''
Implement PatternToNumber
http://rosalind.info/problems/ba1l/

Given: A DNA string Pattern.

Return: PatternToNumber(Pattern).
'''
filename = 'rosalind_ba1l.txt'

def pattern_to_number(pattern):
	values = {
		'A': 0,
		'C': 1,
		'G': 2,
		'T': 3
	}
	return sum([values[base] * (4 ** i) for i, base in enumerate(reversed(pattern))])

def main():
	with open(filename) as f:
		pattern = f.readline().strip()
	print(pattern_to_number(pattern))

if __name__ == '__main__':
	main()
