import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []

graph = list([] for _ in range(n+1))

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)