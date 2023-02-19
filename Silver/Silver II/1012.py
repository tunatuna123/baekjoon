from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def search(x,y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if graph[y][x] == 0:
        return False
    return True

def bfs(x,y):
    if graph[y][x] == 0:
        return False

    queue = deque()
    queue.append((x,y))
    graph[y][x] = 0

    while queue:
        x_coord,y_coord = queue.popleft()
        for i in range(4):
            nex_x,nex_y = x_coord+dx[i],y_coord+dy[i]
            search(nex_x,nex_y)
            if search(nex_x,nex_y):
                queue.append((nex_x,nex_y))
                graph[nex_y][nex_x] = 0
    return True

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    for j in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1
    ans = 0
    for i in range(m):
        for j in range(n):
            if bfs(i,j):
                ans += 1
    print(ans)