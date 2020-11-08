'''
Protein Translation
http://rosalind.info/problems/ptra/

Given: A DNA string s of length at most 10 kbp, and a protein string translated by s.

Return: The index of the genetic code variant that was used for translation. (If multiple solutions exist, you may return any one.)
'''
from Bio.Seq import translate

filename = 'rosalind_ptra.txt'
TABLES = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]

def tranlation_table(dna, protein):
	for table in TABLES:
		if translate(dna, table=table, stop_symbol='') == protein:
			return table

def main():
	with open(filename) as f:
		dna = f.readline().strip()
		protein = f.readline().strip()
	print(tranlation_table(dna, protein))

if __name__ == '__main__':
	main()
