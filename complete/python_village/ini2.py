'''
Variables and Some Arithmetic
http://rosalind.info/problems/ini2/

Given: Two positive integers a and b, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
'''
filename = 'rosalind_ini2.txt'

def sq_hypotenuse(a, b):
	return a ** 2 + b ** 2

def main():
	with open(filename) as f:
		a, b = [int(i) for i in f.readline().strip().split()]
	print(sq_hypotenuse(a, b))

if __name__ == '__main__':
	main()
