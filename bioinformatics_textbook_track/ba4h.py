'''
Generate the Convolution of a Spectrum
http://rosalind.info/problems/ba4h/

Given: A collection of integers Spectrum.

Return: The list of elements in the convolution of Spectrum in decreasing order of their multiplicities. If an element has multiplicity k, it should appear exactly k times.
'''
filename = 'rosalind_ba4h.txt'

def convolution(spectrum):
	spectrum.sort()
	counter = {}
	for i in range(len(spectrum) - 1):
		for j in range(i + 1, len(spectrum)):
			diff = spectrum[j] - spectrum[i]
			counter[diff] = counter.get(diff, 0) + 1
	counter = {k: v for k, v in sorted(counter.items(), key=lambda x: x[1], reverse=True)}
	
	# from questions section: 0 should not be included
	if 0 in counter:
		counter.pop(0)
		
	conv = []
	for k, v in counter.items():
		conv.extend([str(k)] * v)
	return conv
	
def main():
	with open(filename) as f:
		spectrum = list(map(int, f.readline().strip().split()))
	print(*convolution(spectrum))

if __name__ == '__main__':
	main()
