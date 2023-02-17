n = int(input())
for i in range(n):
    k = int(input())
    n = int(input())
    f = [x for x in range(1,n+1)]
    for j in range(k):
        for t in range(1,n):
            f[t] += f[t-1]
    print(f[-1])