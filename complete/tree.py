# minimum edges is n-1

f = open("rosalind_tree.txt", "r")
lines = f.readlines()
f.close()

# lines[0] is number of nodes
# len(lines) is number of edges given

print int(lines[0]) - len(lines) # n nodes must be connected by n-1 edges