'''
Majority Element
http://rosalind.info/problems/maj/

Given: A positive integer k≤20, a positive integer n≤104, and k arrays of size n containing positive integers not exceeding 105.

Return: For each array, output an element of this array occurring strictly more than n/2 times if such element exists, and "-1" otherwise
'''
filename = 'rosalind_maj.txt'

def majority_element(arrs):
	# could do trivially with Counter, but use moore's voting algorithm--O(n) divide and conquer
	majority_elements = []
	for arr in arrs:
		maj_elem, count = arr[0], 0
		for i in arr:
			if i == maj_elem:
				count += 1
			else:
				count -= 1
			if count == 0:
				maj_elem = i
				count = 1
		if sum([i == maj_elem for i in arr]) > len(arr) / 2:
			majority_elements.append(maj_elem)
		else:
			majority_elements.append(-1)
	return majority_elements

def main():
	with open(filename) as f:
		f.readline() # discard--number of arrays, length of arrays
		arrs = [[int(i) for i in line.strip().split()]for line in f.readlines()]
	print(' '.join([str(i) for i in majority_element(arrs)]))

if __name__ == '__main__':
	main()
