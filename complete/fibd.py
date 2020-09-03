import numpy as np

def main():
	n = 89
	m = 16
	arr = [0] * m
	print(arr)
	arr[0] = 1
	for i in range(n-1):
		arr[1:], arr[0] = arr[:-1], sum(arr[1:])
	print(sum(arr))

if __name__ == '__main__':
	main()