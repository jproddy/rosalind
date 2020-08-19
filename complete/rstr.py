f = open("rosalind_rstr_2_dataset.txt", "r")
lines = f.readlines()
f.close()

nums = lines[0].split(" ")

n = int(nums[0]) # number of random strings
gc = float(nums[1]) # GC content
s = lines[1].strip() # desired DNA string

at = s.count("A") + s.count("T")

print 1 - (1 - ((1-gc)/2)**at * (gc/2)**(len(s)-at)) ** n