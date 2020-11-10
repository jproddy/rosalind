'''
Compute the Hamming Distance Between Two Strings
http://rosalind.info/problems/ba1g/

Given: Two DNA strings.

Return: An integer value representing the Hamming distance.
'''
filename = 'rosalind_ba1g.txt'

def hamming_distance(s, t):
	# copied from bioinformatics_stronghold/hamm
	return sum([si != ti for si, ti in zip(s, t)])

def main():
	with open(filename) as f:
		s = f.readline().strip()
		t = f.readline().strip()
	print(hamming_distance(s, t))

if __name__ == '__main__':
	main()
