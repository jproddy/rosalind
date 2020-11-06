'''
Speeding Up Motif Finding
http://rosalind.info/problems/kmp/

Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.
'''
from utils.parse_fasta import parse_fasta_as_list
filename = 'rosalind_kmp.txt'

def failure_array(s):
	failure = [0] * len(s)
	i, curr_len = 1, 0
	while i < len(s):
		if s[i] == s[curr_len]:
			curr_len += 1
			failure[i] = curr_len
			i += 1
		elif curr_len == 0:
			failure[i] = 0
			i += 1
		else:
			curr_len = failure[curr_len-1]
	return failure

def main():
	with open(filename) as f:
		fasta = f.read()
	s = parse_fasta_as_list(fasta)[0]
	print(' '.join(map(str, failure_array(s))))

if __name__ == '__main__':
	main()
