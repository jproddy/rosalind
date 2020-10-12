'''
Conditions and Loops
http://rosalind.info/problems/ini4/

Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.
'''
filename = 'rosalind_ini4.txt'

def loop_sum(a, b):
	return sum([i if i & 1 else 0 for i in range(a, b+1)])

def main():
	with open(filename) as f:
		a, b = [int(i) for i in f.readline().strip().split()]
	print(loop_sum(a, b))

if __name__ == '__main__':
	main()
