'''
Mortal Fibonacci Rabbits
http://rosalind.info/problems/fibd/

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
'''
filename = 'rosalind_fibd.txt'

def mortal_fib_rabbits(n, m):
	# attempting to use this with default numpy arrays leads to precision errors :(
	arr = [1] + [0] * (m - 1)
	for _ in range(n-1):
		arr[1:], arr[0] = arr[:-1], sum(arr[1:])
	return sum(arr)


def main():
	with open(filename) as f:
		line = f.readline().strip()
	n, m = [int(i) for i in line.split()]
	print(mortal_fib_rabbits(n, m))

if __name__ == '__main__':
	main()
