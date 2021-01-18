'''
Counting Unrooted Binary Trees
http://rosalind.info/problems/cunr/

Given: A positive integer n (n≤1000).

Return: The value of b(n) modulo 1,000,000.
'''
filename = 'rosalind_cunr.txt'

def count_ubt(n):
	n = 2 * n - 5
	prod = 1
	while n > 1:
		prod *= n
		prod %= 1000000
		n -= 2
	return prod

def main():
	with open(filename) as f:
		n = int(f.readline().strip())
	print(count_ubt(n))

if __name__ == '__main__':
	main()
