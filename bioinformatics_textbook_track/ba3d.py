'''
Construct the De Bruijn Graph of a String
http://rosalind.info/problems/ba3d/

Given: An integer k and a string Text.

Return:DeBruijnk(Text), in the form of an adjacency list.
'''
filename = 'rosalind_ba3d.txt'

def de_brujin(k, text):
	adj_list = {}
	for i in range(len(text) - k + 1):
		key = text[i:i+k-1]
		val = text[i+1:i+k]
		if key in adj_list:
			adj_list[key].append(val)
		else:
			adj_list[key] = [val]
	return adj_list

def main():
	with open(filename) as f:
		k = int(f.readline().strip())
		text = f.readline().strip()
	for key, val in de_brujin(k, text).items():
		v = ','.join(val)
		print(f'{key} -> {v}')

if __name__ == '__main__':
	main()
