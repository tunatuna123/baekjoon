import sys
input = sys.stdin.readline

n = int(input())
cmd = list(input().strip())

board = [['.' for _ in range(n)] for i in range(n)]
x,y = 0,0

def check():
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()

for k in cmd:
    if k == 'D':
        if board[y][x] == '-':
            board[y][x] = '+'
        else:
            board[y][x] = '|'
        if y+1 < n:
            board[y+1][x] = '|'
            y += 1
    
    elif k == 'U':
        if board[y][x] == '-':
            board[y][x] = '+'
        else:
            board[y][x] = '|'
        if y-1 >= 0:
            board[y-1][x] = '|'
            y -= 1
    
    elif k == 'L':
        if board[y][x] == '|':
            board[y][x] = '+'
        else:
            board[y][x] = '-'
        if x-1 >= 0:
            board[y][x-1] = '-'
            x -= 1
    
    elif k == 'R':
        if board[y][x] == '|':
            board[y][x] = '+'
        else:
            board[y][x] = '-'
        if x+1 < n:
            board[y][x+1] = '-'
            x += 1

check()