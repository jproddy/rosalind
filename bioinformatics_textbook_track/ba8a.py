'''
Implement FarthestFirstTraversal
http://rosalind.info/problems/ba8a/

Given: Integers k and m followed by a set of points Data in m-dimensional space.

Return: A set Centers consisting of k points (centers) resulting from applying FarthestFirstTraversal(Data, k), where the first point from Data is chosen as the first center to initialize the algorithm.
'''
filename = 'rosalind_ba8a.txt'

def farthest_first_traversal(first_point, data, k):
	centers = {first_point}
	for _ in range(k - 1):
		new_center = max(data, key=lambda x: min_euclidian_distance(x, centers))
		data.remove(new_center)
		centers.add(new_center)
	return centers	

def min_euclidian_distance(p, centers):
	return min(sum((i - j) ** 2 for i, j in zip(p, q)) ** 0.5 for q in centers)

def main():
	with open(filename) as f:
		k, _ = tuple(map(int, f.readline().strip().split()))
		first_point = tuple(map(float, f.readline().strip().split()))
		data = {tuple(map(float, line.strip().split())) for line in f.readlines()}
	for point in farthest_first_traversal(first_point, data, k):
		print(*point)

if __name__ == '__main__':
	main()
