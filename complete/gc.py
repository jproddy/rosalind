'''
Computing GC Content
http://rosalind.info/problems/gc/

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''
from utils.parse_fasta import parse_fasta_as_dict

filename = 'rosalind_gc.txt'

def max_gc_content(strings):
    max_gc = 0
    max_id = ''
    for fasta_id, string in strings.items():
        gc_count = sum([ char == 'C' or char == 'G' for char in string])
        gc_ratio = gc_count / len(string)
        if gc_ratio > max_gc:
            max_gc = gc_ratio
            max_id = fasta_id
    return max_id, max_gc

def main():
    with open(filename) as f:
        fasta = f.read()
    strings = parse_fasta_as_dict(fasta)
    fasta_id, gc = max_gc_content(strings)
    print(fasta_id, '\n', gc * 100)

if __name__ == '__main__':
    main()
