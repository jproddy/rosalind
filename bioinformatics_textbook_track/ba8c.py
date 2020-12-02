'''
Implement the Lloyd Algorithm for k-Means Clustering
http://rosalind.info/problems/ba8c/

Given: Integers k and m followed by a set of points Data in m-dimensional space.

Return: A set Centers consisting of k points (centers) resulting from applying the Lloyd algorithm to Data and Centers, where the first k points from Data are selected as the first k centers.
'''
import numpy as np

from ba8a import min_euclidian_distance

filename = 'rosalind_ba8c.txt'

def lloyd(centers, data):
	k = len(centers)
	old_centers = {}
	while old_centers != centers:
		old_centers = centers
		centers = {center: [] for center in old_centers}
		for point in data:
			nearest_center = min(old_centers, key=lambda x: euclidian_distance(x, point))
			centers[nearest_center].append(point)
		centers = {tuple(sum(np.array(point) for point in points) / len(points)) for points in centers.values()}
		# print(centers)
	return centers

def euclidian_distance(p, q):
	return sum((i - j) ** 2 for i, j in zip(p, q)) ** 0.5

def main():
	with open(filename) as f:
		k, _ = tuple(map(int, f.readline().strip().split()))
		centers = [tuple(map(float, f.readline().strip().split())) for _ in range(k)]
		data = [tuple(map(float, line.strip().split())) for line in f.readlines()]
	data.extend(centers)
	for point in lloyd(centers, data):
		print(*point)

if __name__ == '__main__':
	main()
