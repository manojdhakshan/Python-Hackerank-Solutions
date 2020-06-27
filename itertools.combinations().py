from itertools import combinations
a=input()
x=a.split()
b=sorted(x[0])
#print(type(x[-1]))
#c=(list(combinations(b,int(x[-1]))))
r=[]
for i in range(1,int(x[-1])+1):
    y=(list(combinations(b,i)))
    r.append(list(y))
p=[]
for j in r:
    for k in j:
        p.append(k)
for l in p:
    print("".join(l))
    
