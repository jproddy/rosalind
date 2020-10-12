'''
Counting Subsets
http://rosalind.info/problems/sset/

Given: A positive integer n (n≤1000).

Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.
'''
filename = 'rosalind_sset.txt'

def subsets(n):
	# every element is either in or out of a given subset
	return 2 ** n

def main():
	with open(filename) as f:
		n = int(f.readline().strip())
	print(subsets(n) % 1000000)

if __name__ == '__main__':
	main()
