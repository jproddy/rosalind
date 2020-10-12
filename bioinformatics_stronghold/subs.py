'''
Finding a Motif in DNA
http://rosalind.info/problems/subs/

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
'''
filename = 'rosalind_subs.txt'

def substring_locations(s, t):
	# alternatively could be done with any number of string index/regex methods
	locations = []
	for i in range(len(s) - len(t)):
		if s[i : i+len(t)] == t:
			locations.append(i + 1)
	return locations

def main():
	with open(filename) as f:
		s = f.readline().strip()
		t = f.readline().strip()
	print(' '.join([str(i) for i in substring_locations(s, t)]))

if __name__ =='__main__':
	main()
