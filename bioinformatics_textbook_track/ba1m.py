'''
Implement NumberToPattern
http://rosalind.info/problems/ba1m/

Given: Integers index and k.

Return: NumberToPattern(index, k).
'''
filename = 'rosalind_ba1m.txt'

def number_to_pattern(index, k):
	values = {
		0: 'A',
		1: 'C',
		2: 'G',
		3: 'T'
	}
	return ''.join([values[(index // (4 ** i)) % 4] for i in range(k-1, -1, -1)])

def main():
	with open(filename) as f:
		index = int(f.readline().strip())
		k = int(f.readline().strip())
	print(number_to_pattern(index, k))

if __name__ == '__main__':
	main()
