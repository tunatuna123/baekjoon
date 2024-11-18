n,m,v = map(int,input().split())

graph = [[] for x in range(n+1)]
visited = [False]*(n+1)
dfs = []
bfs = []

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def DFS(v):
    visited[v] = True
    dfs.append(v)
    for i in graph[v]:
        if visited[i] == False:
            DFS(i)

def BFS(v):
    visited[v] = True
    bfs.append(v)
    queue = [v]
    while queue:
        for i in graph[queue.pop(0)]:
            if visited[i] == False:
                visited[i] = True
                bfs.append(i)
                queue.append(i)

DFS(v)
visited = [False]*(n+1)
BFS(v)

print(' '.join(list(map(str,dfs))))
print(' '.join(list(map(str,bfs))))