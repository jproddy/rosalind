from itertools import groupby
with open("rosalind_lcsm.txt") as f:
    groups = groupby(f, key=lambda x: not x.startswith(">"))
    d = {}
    for k,v in groups:
        if not k:
            key, val = list(v)[0].rstrip(), "".join(map(str.rstrip,next(groups)[1],""))
            d[key] = val
f.close()
#print(d)

vals = d.values()
l = len(vals[0])
high = 0
highword = ""

for i in range(l):
    for j in reversed(range(l)):
        if i + j < l:
            if all(vals[0][i:i+j] in val for val in vals) and j > high:
                high = j
                highword = vals[0][i:i+j]
                #print high
                #print highword

#print high
print highword