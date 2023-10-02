from collections import deque

def bfs(start,end):
    visited = [False]*(n+1)
    dist = [0]*(n+1)
    q = deque([start])
    while q:
        now = q.popleft()
        if now == end:
            break
        if visited[now] == False:
            visited[now] = True
            for i in graph[now]:
                q.append(i[0])
                dist[i[0]] = dist[now] + i[1]
    return dist[end]

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]

for i in range(n-1):
    a,b,d = map(int,input().split())
    graph[a].append((b,d))
    graph[b].append((a,d))

for i in range(m):
    a,b = map(int,input().split())
    print(bfs(a,b))