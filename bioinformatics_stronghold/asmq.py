'''
Assessing Assembly Quality with N50 and N75
http://rosalind.info/problems/asmq/

Given: A collection of at most 1000 DNA strings (whose combined length does not exceed 50 kbp).

Return: N50 and N75 for this collection of strings.
'''
filename = 'rosalind_asmq.txt'

def assembly_quality(dnas):
	len_counter = {}
	total_bp = 0
	for dna in dnas:
		l = len(dna)
		total_bp += l
		len_counter[l] = len_counter.get(l, 0) + 1
	sorted_lens = sorted(len_counter, reverse=True)
	n50, n75 = 0, 0
	curr_bp = 0
	for s_len in sorted_lens:
		curr_bp += s_len * len_counter[s_len]
		curr_rat = curr_bp / total_bp
		if (not n50) and curr_rat >= 0.5:
			n50 = s_len
		if (not n75) and curr_rat >= 0.75:
			n75 = s_len
		if n50 and n75:
			return n50, n75

def main():
	with open(filename) as f:
		lines = [line.strip() for line in f.readlines()]
	print(*assembly_quality(lines))

if __name__ == '__main__':
	main()
