'''
Find All Approximate Occurrences of a Pattern in a String
http://rosalind.info/problems/ba1h/

Given: Strings Pattern and Text along with an integer d.

Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
'''
filename = 'rosalind_ba1h.txt'

def approx_occurances(pattern, text, d):
	lp = len(pattern)
	return [i for i in range(len(text) - lp + 1) if sc_hamming_distance(pattern, text[i:i+lp], d)]

def sc_hamming_distance(s, t, d):
	# probably doesnt improve runtime substantially unless pattern is long
	# and may even slow down when pattern is short
	mismatches = 0
	for i in range(len(s)):
		mismatches += s[i] != t[i]
		if mismatches > d:
			return False
	return True

def main():
	with open(filename) as f:
		pattern = f.readline().strip()
		text = f.readline().strip()
		d = int(f.readline().strip())
	print(*approx_occurances(pattern, text, d))

if __name__ == '__main__':
	main()
