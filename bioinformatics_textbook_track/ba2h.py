'''
Implement DistanceBetweenPatternAndStrings
http://rosalind.info/problems/ba2h/

Given: A DNA string Pattern and a collection of DNA strings Dna.

Return: DistanceBetweenPatternAndStrings(Pattern, Dna).
'''
from ba1g import hamming_distance

filename = 'rosalind_ba2h.txt'

def distance_between_pattern_and_strings(pattern, dnas):
	l = len(pattern)
	distance = 0
	for dna in dnas:
		distance += min(hamming_distance(pattern, dna[i:i+l]) for i in range(len(dna) - l + 1))
	return distance

def main():
	with open(filename) as f:
		pattern = f.readline().strip()
		dnas = f.readline().strip().split()
	print(distance_between_pattern_and_strings(pattern, dnas))

if __name__ == '__main__':
	main()
