'''
Rabbits and Recurrence Relations
http://rosalind.info/problems/fib/

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
'''
filename = 'rosalind_fib.txt'

def fib_rabbits(n, k):
	prev, curr = 1, 1
	for _ in range(2, n):
		prev, curr = curr, k * prev + curr
	return curr
	# alternatively, keep full list in memory:
	# fib = [1, 1]
	# for i in range(2, n):
	# 	fib.append(k * fib[i-2]  fib[i-1])
	# return fib[-1]

def main():
	with open(filename) as f:
		line = f.readline().strip()
	# months, litter size
	n, k = (int(i) for i in line.split(' '))
	print(fib_rabbits(n, k))

if __name__ == '__main__':
	main()
