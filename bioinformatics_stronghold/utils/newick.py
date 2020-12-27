import re

class NewickNode:
	def __init__(self, name=None, value=0, children=None, parent=None):
		self.name = name
		self.value = value # edge weight to/from parent
		self.parent = parent
		self.children = children if children else []

class NewickParser:
	def __init__(self):
		pass

	def parse(self, s):
		'''
		parses a VALID newick tree
		for a more comprehensive regex version, see biopython:
			https://github.com/biopython/biopython/blob/master/Bio/Phylo/NewickIO.py
		'''
		single_char_groups = {'(', ')', ','}
		ending_chars = {'(', ')', ',', ':', ';'}

		groups = []
		i = 0
		while i < len(s):
			if s[i] in single_char_groups:
				groups.append(s[i])
				i += 1
			elif s[i] == ';':
				groups.append(s[i])
				break
			elif s[i] == ':': # start 
				start = i
				i += 1
				while s[i] not in ending_chars:
					i += 1
				groups.append(s[start:i])
			else: # name
				start = i
				while s[i] not in ending_chars:
					i += 1
				groups.append(s[start:i])

		root_node = NewickNode()
		curr_node = root_node

		for group in groups:
			if group[0] == '(':
				new_node = NewickNode(parent=curr_node)
				curr_node.children.append(new_node)
				curr_node = new_node
			elif group[0] == ')':
				curr_node = curr_node.parent
			elif group[0] == ',':
				if curr_node is root_node:
					root_node = NewickNode(children=[curr_node])
					curr_node.parent = root_node
				curr_node = NewickNode(parent=curr_node.parent)
				curr_node.parent.children.append(curr_node)
			elif group[0] == ':':
				curr_node.value = float(group[1:])
			elif group[0] == ';':
				break
			else:
				curr_node.name = group

		return root_node
