INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF]*(n+1) for x in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1,n+1):
    for j in range(1,m+1):
        if i == j:
            graph[i][j] = 0

for k in range(1,n+1):
    for j in range(1,n+1):
        for i in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

ans = {}
for i in range(1,n+1):
    ans[i] = sum(graph[i][1:])
print(sorted(ans.items(), key=lambda x: x[1])[0][0])