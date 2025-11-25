n = int(input())
a = list(map(int, input().split()))
m = int(input())

for i in range(m):
    ans = 0
    k,l,r = map(int, input().split())
    if k == 1:
        for j in range(l-1,r):
            a[j] = a[j]**2 % 2010
    elif k == 2:
        for j in range(l-1,r):
            ans += a[j]
        print(ans)