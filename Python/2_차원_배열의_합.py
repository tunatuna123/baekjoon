import sys
input = sys.stdin.readline

m,n = map(int,input().split())
lst = []

for i in range(m):
    lst.append(list(map(int,input().split())))

k = int(input())

for _ in range(k):
    ans = 0
    i,j,x,y = map(int,input().split())
    for p in range(j-1,y):
        for q in range(i-1,x):
            ans += lst[q][p]
    print(ans)