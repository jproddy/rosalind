'''
Compute the Squared Error Distortion
http://rosalind.info/problems/ba8b/

Given: Integers k and m, followed by a set of centers Centers and a set of points Data.

Return: The squared error distortion Distortion(Data, Centers).
'''
from ba8a import min_euclidian_distance

filename = 'rosalind_ba8b.txt'

def distortion(data, centers):
	return sum(min_euclidian_distance(point, centers) ** 2 for point in data) / len(data)

def main():
	with open(filename) as f:
		k, _ = tuple(map(int, f.readline().strip().split()))
		centers = set()
		for _ in range(k):
			centers.add(tuple(map(float, f.readline().strip().split())))
		f.readline()
		data = {tuple(map(float, line.strip().split())) for line in f.readlines()}
	print(distortion(data, centers))

if __name__ == '__main__':
	main()
