import sys
input = sys.stdin.readline

n = int(input())

board = []
ans = list(list('*'*n) for _ in range(n))

dy = [1,1,1,0,0,-1,-1,-1]
dx = [0,-1,1,-1,1,0,-1,1]

for i in range(n):
    board.append(list(input().strip()))

for y in range(n):
    for x in range(n):
        if board[y][x].isdigit():
            ans[y][x] = '*'
        else:
            t = 0
            for i in range(8):
                if y+dy[i] < 0 or y+dy[i] >= n or x+dx[i] < 0 or x+dx[i] >= n:
                    continue
                else:
                    if board[y+dy[i]][x+dx[i]].isdigit():
                        t += int(board[y+dy[i]][x+dx[i]])
            if t >= 10:
                ans[y][x] = 'M'
            else:
                ans[y][x] = t

for i in range(n):
    for j in range(n):
        print(ans[i][j], end='')
    print()