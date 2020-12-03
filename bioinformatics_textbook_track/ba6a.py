'''
Implement GreedySorting to Sort a Permutation by Reversals
http://rosalind.info/problems/ba6a/

Given: A signed permutation P.

Return: The sequence of permutations corresponding to applying GreedySorting to P, ending with the identity permutation.
'''
filename = 'rosalind_ba6a.txt'

def greedy_sorting(P):
	for i in range(len(P)):
		if i + 1 != abs(P[i]):
			for j in range(i + 1, len(P)):
				if i + 1 == abs(P[j]):
					P[i:j+1] = reversed(P[i:j+1])
					P[i:j+1] = [-val for val in P[i:j+1]]
					break
			formatted_print(P)

		if P[i] < 0:
			P[i] = abs(P[i])
			formatted_print(P)

	return P

def formatted_print(P):
	print('(' + ' '.join(str(i) if i < 0 else '+' + str(i) for i in P) + ')')

def main():
	with open(filename) as f:
		P = list(map(int, f.readline().strip()[1:-1].split()))
	greedy_sorting(P)

if __name__ == '__main__':
	main()
