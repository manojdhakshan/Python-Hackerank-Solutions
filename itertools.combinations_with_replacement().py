from itertools import combinations_with_replacement as rp
a=input()
x=a.split()
b=sorted(x[0])
c=(list(rp(b,int(x[-1]))))
for i in c:
    print("".join(i))
