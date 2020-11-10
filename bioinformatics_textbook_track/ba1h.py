'''
Find All Approximate Occurrences of a Pattern in a String
http://rosalind.info/problems/ba1h/

Given: Strings Pattern and Text along with an integer d.

Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
'''
from ba1g import hamming_distance

filename = 'rosalind_ba1h.txt'

def approx_occurances(pattern, text, d):
	lp = len(pattern)
	# could also implement a short circuiting hamming distance to quit
	# evaluation once the distance is greater than d
	return [i for i in range(len(text) - lp + 1) if hamming_distance(pattern, text[i:i+lp]) <= d]

def main():
	with open(filename) as f:
		pattern = f.readline().strip()
		text = f.readline().strip()
		d = int(f.readline().strip())
	print(*approx_occurances(pattern, text, d))

if __name__ == '__main__':
	main()
