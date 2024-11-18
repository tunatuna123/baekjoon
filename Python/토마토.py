import sys
from collections import deque
input = sys.stdin.readline

w,h = map(int,input().split())
box = []

for _ in range(h):
    box.append(list(map(int,input().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
tomato = deque([])
ans = 0

for i in range(h):
    for j in range(w):
        if box[i][j] == 1:
            tomato.append([i,j])


def bfs():
    while tomato:
        y,x = tomato.popleft()
        for i in range(4):
            ty, tx = y + dy[i], x + dx[i]
            if 0 <= ty < h and 0 <= tx < w and box[ty][tx] == 0:
                box[ty][tx] = box[y][x] + 1
                tomato.append([ty,tx])


bfs()
for i in range(h):
    for j in range(w):
        if box[i][j] == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(box[i]))
print(ans-1)