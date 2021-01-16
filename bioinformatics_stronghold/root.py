'''
Counting Rooted Binary Trees
http://rosalind.info/problems/root/

Given: A positive integer n (n≤1000).

Return: The value of B(n) modulo 1,000,000.
'''
filename = 'rosalind_root.txt'

def count_rbt(n):
	n = (2 * n) - 3
	prod = 1
	while n > 1:
		prod *= n
		prod %= 1000000
		n -= 2
	return prod

def main():
	with open(filename) as f:
		n = int(f.readline().strip())
	print(count_rbt(n))

if __name__ == '__main__':
	main()
