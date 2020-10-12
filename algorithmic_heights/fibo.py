'''
Fibonacci Numbers
http://rosalind.info/problems/fibo/

Given: A positive integer n≤25.

Return: The value of Fn.
'''
filename = 'rosalind_fibo.txt'

def fibonacci(n):
	prev, curr = 1, 1
	for _ in range(2, n):
		prev, curr = curr, prev + curr
	return curr

def main():
	with open(filename) as f:
		n = int(f.readline().strip())
	print(fibonacci(n))

if __name__ == '__main__':
	main()
