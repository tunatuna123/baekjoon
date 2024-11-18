import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(input().strip()))

queue = deque([(0,0)])
dy, dx = [0,0,-1,1], [-1,1,0,0]

while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
            if arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1

print(arr[n-1][m-1])