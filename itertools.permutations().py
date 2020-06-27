from itertools import permutations
a=input()
x=a.split()
b=sorted(x[0])
#print(type(x[-1]))
c=(list(permutations(b,int(x[-1]))))
for i in c:
    print("".join(i))
