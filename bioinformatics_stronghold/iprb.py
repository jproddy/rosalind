'''
Mendel's First Law
http://rosalind.info/problems/iprb/

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
'''
filename = 'rosalind_iprb.txt'

def p_dominant(k, m, n):
	population = k + m + n
	# calculate 1 - P(homozygous recessive)
	x = (0.5 ** 2) * m * (m - 1)	# heterozygous x heterozygous
	y = 1 * 0.5 * 2 * m * n			# heterozygous x homozygous recessive
	z = (1 ** 2) * n * (n - 1)			# homozygous recessive x homozygous recessive
	return 1 - ((x + y + z) / (population * (population - 1)))

def main():
	with open(filename) as f:
		line = f.readline().strip()
	# homozygous dominant, heterozygous, homozygous recessive
	k, m, n = (int(i) for i in line.split(' '))
	print(p_dominant(k, m, n))
	
if __name__ == '__main__':
	main()
