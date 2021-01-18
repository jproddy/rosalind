'''
Compute Limb Lengths in a Tree
http://rosalind.info/problems/ba7b/

Given: An integer n, followed by an integer j between 0 and n - 1, followed by a space-separated additive distance matrix D (whose elements are integers).

Return: The limb length of the leaf in Tree(D) corresponding to row j of this distance matrix (use 0-based indexing).
'''
filename = 'rosalind_ba7b.txt'

def limb_length(j, arr):
	return min(
		(arr[i][j] + arr[j][k] - arr[i][k]) // 2
		for i in range(len(arr))
		for k in range(len(arr))
		if (i != j) and (i != k) and (j != k)
	)

def main():
	with open(filename) as f:
		f.readline()
		j = int(f.readline().strip())
		arr = [list(map(int, line.strip().split())) for line in f.readlines()]
	print(limb_length(j, arr))

if __name__ == '__main__':
	main()
