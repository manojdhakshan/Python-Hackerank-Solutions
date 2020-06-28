a,b=(int(input()),input().split())
c,d=(int(input()),input().split())
e=list(map(int,b))
f=list(map(int,d))
a=[]
for i in e:
    if i not in f:
        a.append(i)
for j in f:
    if j not in e:
        a.append(j)
x=(sorted(set(a)))
for k in x:
    print(k)
