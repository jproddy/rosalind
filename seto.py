f = open("rosalind_seto.txt", "r")
lines = f.readlines()
f.close()

n = int(lines[0].strip())
A = {int(x) for x in lines[1].strip().strip("{").strip("}").split(", ")}
B = {int(x) for x in lines[2].strip().strip("{").strip("}").split(", ")}

N=set(range(1,n+1))

#union
print list(A|B).__str__().replace('[','{').replace(']','}')

#intersection
print list(A&B).__str__().replace('[','{').replace(']','}')

#A-B
print list(A-B).__str__().replace('[','{').replace(']','}')

#B-A
print list(B-A).__str__().replace('[','{').replace(']','}')

#Ac = N-A
print list(N-A).__str__().replace('[','{').replace(']','}')

#Bc = N-B
print list(N-B).__str__().replace('[','{').replace(']','}')
