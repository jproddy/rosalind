'''
Find a Profile-most Probable k-mer in a String
http://rosalind.info/problems/ba2c/

Given: A string Text, an integer k, and a 4 × k matrix Profile.

Return: A Profile-most probable k-mer in Text. (If multiple answers exist, you may return any one.)
'''
from functools import reduce
import pandas as pd

filename = 'rosalind_ba2c.txt'
BASES = ['A' , 'C', 'G', 'T']

def profile_most_probable(text, k, profile):
	max_p = float('-inf')
	for i in range(len(text) - k + 1):
		substring = text[i:i+k]
		p = reduce(lambda x, y: x * y, [profile.loc[base, i] for i, base in enumerate(substring)])
		if p > max_p:
			max_p = p
			max_str = substring
	return max_str

def main():
	with open(filename) as f:
		text = f.readline().strip()
		k = int(f.readline().strip())
		data = [line.strip().split() for line in f.readlines()]
		profile = pd.DataFrame(data, index=BASES, dtype=float)
	print(profile_most_probable(text, k, profile))

if __name__ == '__main__':
	main()
