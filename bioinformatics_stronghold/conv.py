'''
Comparing Spectra with the Spectral Convolution
http://rosalind.info/problems/conv/

Given: Two multisets of positive real numbers S1 and S2. The size of each multiset is at most 200.

Return: The largest multiplicity of S1⊖S2, as well as the absolute value of the number x maximizing (S1⊖S2)(x) (you may return any such value if multiple solutions exist).
'''
filename = 'rosalind_conv.txt'
ROUND = 5

def max_mult_spec_conv_shift(S1, S2):
	shifts = {}
	for i in S1:
		for j in S2:
			diff = round(i - j, ROUND)
			shifts[diff] = shifts.get(diff, 0) + 1
	max_mult_shift = max(shifts, key=lambda x: shifts[x])
	return shifts[max_mult_shift], abs(max_mult_shift)

def main():
	with open(filename) as f:
		S1 = list(map(float, f.readline().strip().split()))
		S2 = list(map(float, f.readline().strip().split()))
	print(*max_mult_spec_conv_shift(S1, S2), sep='\n')

if __name__ == '__main__':
	main()
