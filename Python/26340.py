n = int(input())
for i in range(n):
    a,b,t = map(int,input().split())
    print('Data set:',a,b,t)
    for j in range(t):
        if a > b:
            a //= 2
        else:
            b //= 2
    print(max(a,b),min(a,b))
    if i != n-1:
        print()