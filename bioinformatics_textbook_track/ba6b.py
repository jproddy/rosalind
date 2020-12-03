'''
Compute the Number of Breakpoints in a Permutation
http://rosalind.info/problems/ba6b/

Given: A signed permutation P.

Return: The number of breakpoints in P.
'''
filename = 'rosalind_ba6b.txt'

def n_breakpoints(P):
	# not defined in the problem, but breakpoints correspond to the number
	# of i such that P_i + 1 != P_i+1 with an imaginary 0 at the beginning of P
	# and imaginary len(P) + 1 at the end
	breakpoints = (P[0] != 1) + (P[-1] != len(P))
	breakpoints += sum(P[i] + 1 !=  P[i+1] for i in range(len(P) - 1))
	return breakpoints

def main():
	with open(filename) as f:
		P = list(map(int, f.readline().strip()[1:-1].split()))
	print(n_breakpoints(P))

if __name__ == '__main__':
	main()
