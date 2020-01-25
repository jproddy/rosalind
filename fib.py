f = open("rosalind_fib.txt", "r")
s = f.read()
f.close()

slist = [int(x) for x in s.split(" ")]

n = slist[0] # months
k = slist[1] # litter pairs

fn = [1,1]

for i in range(2,n):
	fn.append(k * fn[i-2] + fn[i-1])


print fn[n-1]