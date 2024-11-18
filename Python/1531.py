pic = [[0]*100 for x in range(100)]
n,m = map(int,input().split())
ans = 0

for _ in range(n):
    a,b,c,d = map(int,input().split())
    x1,y1 = a,d
    x2,y2 = c,b
    for i in range(100-y1,100-y2+1):
        for j in range(x1-1,x2):
            pic[i][j] += 1

for i in range(100):
    for j in range(100):
        if pic[i][j] > m:
            ans += 1

print(ans)