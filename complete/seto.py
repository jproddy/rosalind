'''
Introduction to Set Operations
http://rosalind.info/problems/seto/

Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.

Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are taken with respect to {1,2,…,n}).
'''
filename = 'rosalind_seto.txt'

def union(A, B):
	return A | B
	# alternatively, 
	# u = A.copy()
	# for element in B:
	# 	if element not in u:
	# 		u.add(element)
	# return u

def intersection(A, B):
	return A & B
	# alternatively,
	# i = set()
	# for element in A: # can optimize by using the smaller of the sets here
	# 	if element in B:
	# 		i.add(element)
	# return i

def set_difference(A, B):
	return A - B
	# alternatively,
	# d = set()
	# for element in A:
	# 	if element not in B:
	# 		d.add(element)
	# return d

def complement(A, n):
	# wrt {1,2,...,n}
	return set(range(1, n+1)) - A

def main():
	with open(filename) as f:
		n = int(f.readline().strip())
		A = {int(i) for i in f.readline().strip()[1:-1].split(', ')}
		B = {int(i) for i in f.readline().strip()[1:-1].split(', ')}
	print(union(A, B))
	print(intersection(A, B))
	print(set_difference(A, B))
	print(set_difference(B, A))
	print(complement(A, n))
	print(complement(B, n))

if __name__ == '__main__':
	main()
