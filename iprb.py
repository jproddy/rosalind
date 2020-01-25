f = open("rosalind_iprb.txt", "r")
s = f.read()
f.close()

slist = [int(x) for x in s.split(" ")]
#print slist

homod = slist[0]
het = slist[1]
homor = slist[2]
tot = homod + het + homor

#calc num rec
a = 0.25 * het * (het - 1) # het het
b = 0.5 * 2 * het * homor # het homor
c = 1.0 * homor * (homor - 1) # homor homor

# print((a+b+c)/(tot*(tot-1))
print(a)
print(b)
print(c)

print(1-((a+b+c)/(tot*(tot-1))))