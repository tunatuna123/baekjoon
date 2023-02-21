def ans(p,q):
    return p%(10**q)//(10**(q-1))
while True:
    a,b = map(int,input().split())
    c,d = 0,0
    if (a,b) == (0,0):
        break
    for i in range(1,len(str(max(a,b)))+1):
        k,t = ans(a,i),ans(b,i)
        if (k+t+c) >= 10:
            d += 1
            c = 1
        else:
            c = 0
    print(d)