import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

queue = deque([])
visited = [[False] * m for _ in range(n)]
ans = [[0]*m for _ in range(n)]
dx, dy = [0,0,1,-1], [1,-1,0,0]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            queue.append((i,j))
            visited[i][j] = True

while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<= nx < n and 0<= ny < m and arr[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            ans[nx][ny] = ans[x][y] + 1
            queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            print(-1, end = ' ')
        else:
            print(ans[i][j], end = ' ')
    print()