'''
Creating a Restriction Map
http://rosalind.info/problems/pdpl/

Given: A multiset L containing (n2) positive integers for some positive integer n.

Return: A set X containing n nonnegative integers such that ΔX=L.
'''
filename = 'rosalind_pdpl.txt'

def solve_turnpike(L):
	# full solution is very slight edit of ba4m
	# based on description, can assume that a correct A exists
	# because L is strictly increasing, can also assume that A has no duplicate points
	L.sort()
	counter = {} # tracks remaining values from L
	for i in L[:-2]:
		counter[i] = counter.get(i, 0) + 1

	A = {0, L[-1], L[-2]}
	counter[L[-1] - L[-2]] -= 1 # this val must exist if problem is solvable
	if not counter[L[-1] - L[-2]]:
		counter.pop(L[-1] - L[-2])

	return sorted(recurse(A.copy(), counter.copy()))

def recurse(A, L):
	# base case
	if not L:
		return A

	max_L = max(L)

	# attempt to add max(L) to A
	if all([abs(max_L - i) in L for i in A]):
		A_copy = A.copy()
		L_copy = L.copy()
		for i in A_copy:
			val = abs(max_L - i)
			L_copy[val] -= 1
			if not L_copy[val]:
				L_copy.pop(val)
		A_copy.add(max_L)
		deeper = recurse(A_copy, L_copy)
		if deeper:
			return deeper

	# if this is invalid, try adding max(A) - max(L) instead
	new_val = max(A) - max_L
	if all([abs(new_val - i) in L for i in A]):
		for i in A:
			val = abs(new_val - i)
			L[val] -= 1
			if not L[val]:
				L.pop(val)
		A.add(new_val)
		deeper = recurse(A.copy(), L.copy())
		if deeper:
			return deeper

	# if both are invalid, a previous choice made this subproblem unsolvable
	return {}

def main():
	with open(filename) as f:
		L = list(map(int, f.readline().strip().split()))
	print(*solve_turnpike(L))

if __name__ == '__main__':
	main()
