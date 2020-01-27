import math
import operator as op
from functools import reduce

def ncr(n, r): # n choose r!
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def progress(prev_gen_probs, ptable): # given previous gen probabilities, convert to new gen probs
	new_gen_probs=[]
	for i in range(2*N+1):
		new_gen_probs.append(0)
		for j in range(2*N+1):
			new_gen_probs[i] += prev_gen_probs[j] * ptable[j][i]
	return new_gen_probs

f = open("rosalind_wfmd.txt", "r")
s = f.read()
f.close()

slist = [int(x) for x in s.split(" ")]

N = slist[0]
m = slist[1]
g = slist[2]
k = slist[3]

dom = m / (2.0 * N) # probability of dominant in g0
rec = 1 - dom # probability of recessive in g0

g1 = [] # probability distribution of recessive allele in g1

for i in range(0, 2*N+1):
	g1.append(ncr(2*N, i) * rec**i * dom**(2*N-i))

probtable = [] 
# GENERATES A 2D ARRAY WHERE i IS THE NUMBER OF REC ALLELES IN PREVIOUS GEN
# and j is REC ALLELES IN NEXT GEN GIVEN i
# PROBABILITY TABLE
for i in range(2*N+1): 
	recnew = i / (2.0 * N)
	domnew = 1 - recnew
	probtable.append([])
	for j in range(2*N+1):
		probtable[i].append(ncr(2*N, j) * recnew**j * domnew**(2*N-j))
# END TABLE GEN

# progress / calc distribution over g generations
prevgen = g1
newgen = []
for i in range(g-1):
	newgen = progress(prevgen, probtable)
	prevgen = newgen

print sum(newgen[k:])



