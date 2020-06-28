if __name__ == '__main__':
    c=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a=(name,score)
        b=(list(a))
        c.append(b)
    d=[]
    for i in c:
        d.append(i[1])
    m=sorted(set(d))
    x=m[1]
    #print(m,x)
    e=[]
    for j in c:
        if x==j[1]:
            e.append(j[0])
    f=(sorted(e))
    for r in f:
        print(r)

