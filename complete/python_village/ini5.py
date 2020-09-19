'''
Working with Files
http://rosalind.info/problems/ini5/

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
'''
filename = 'rosalind_ini5.txt'

def even_lines(lines):
	new_lines = []
	for i, line in enumerate(lines):
		# 1-based numbering
		if i & 1:
			new_lines.append(line)
	return new_lines

def main():
	with open(filename) as f:
		lines = f.readlines()
	new_lines = even_lines(lines)
	output_filename = 'rosalind_ini5_output.txt'
	with open(output_filename, 'w') as f:
		for line in new_lines:
			f.write(line)
			print(line.strip())


if __name__ == '__main__':
	main()
