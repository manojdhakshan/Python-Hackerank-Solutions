a=list(map(int,input().split()))
b=list(map(int,input().split()))
from itertools import product
x=list(product(a,b))
for i in x:
    print(i,end=" ")
