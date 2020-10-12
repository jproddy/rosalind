'''
Strings and Lists
http://rosalind.info/problems/ini3/

Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
'''
filename = 'rosalind_ini3.txt'

def strings(s, a, b, c, d):
	return [s[a:b+1], s[c:d+1]]

def main():
	with open(filename) as f:
		s = f.readline().strip()
		a, b, c, d = [int(i) for i in f.readline().strip().split()]
	print(' '.join(strings(s, a, b, c, d)))

if __name__ == '__main__':
	main()
