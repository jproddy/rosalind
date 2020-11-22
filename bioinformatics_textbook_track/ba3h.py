'''
Reconstruct a String from its k-mer Composition
http://rosalind.info/problems/ba3h/

Given: An integer k followed by a list of k-mers Patterns.

Return: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)
'''
filename = 'rosalind_ba3h.txt'

def reconstruct_string(patterns):
	k = len(patterns[0])
	text = patterns[0]
	suffixes, prefixes = {}, {}
	for p in patterns[1:]:
		suffixes[p[:-1]] = suffixes.get(p[:-1], []) + [p[-1]]
		prefixes[p[1:]] = prefixes.get(p[1:], []) + [p[0]]

	# append suffixes one-by-one until reach end of text
	# each pattern used is then removed from both suffixes and prefixes
	while True:
		s = text[-k+1:]
		if s in suffixes:
			c = suffixes[s].pop()
			if not suffixes[s]:
				suffixes.pop(s)
			text += c
			s += c
			prefixes[s[1:]].remove(s[0])
			if not prefixes[s[1:]]:
				prefixes.pop(s[1:])
		else:
			break

	# then append prefixes similarly but don't need to track removals from suffixes
	while prefixes:
		s = text[:k-1]
		c = prefixes[s].pop()
		if not prefixes[s]:
			prefixes.pop(s)
		text = c + text

	return text

def main():
	with open(filename) as f:
		patterns = [line.strip() for line in f.readlines()[1:]]
	print(reconstruct_string(patterns))

if __name__ == '__main__':
	main()
