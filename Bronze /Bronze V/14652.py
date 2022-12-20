n,m,k = map(int,input().split())
cnt = 0

for i in range(n):
    for j in range(m):
        if cnt == k:
            print(i,j)
        cnt += 1