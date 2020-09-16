'''
Counting Point Mutations
http://rosalind.info/problems/hamm/

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)
'''
filename = 'rosalind_hamm.txt'


def hamming_distance(s, t):
	return sum([si != ti for si, ti in zip(s, t)])

def main():
	with open(filename) as f:
		s = f.readline().strip()
		t = f.readline().strip()
	print(hamming_distance(s, t))

if __name__ == '__main__':
	main()
