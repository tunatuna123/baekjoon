import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    input()
    y,x = map(int,input().split())
    board = []
    ans = 0
    
    for i in range(y):
        board.append(list(input()))
    for i in range(y):
        for j in range(x):
            if board[i][j] == 'o':
                if (i+1<y and i-1>=0) and (board[i+1][j] == '^' and board[i-1][j] == 'v'):
                    ans += 1
                elif (j+1<x and j-1>=0) and (board[i][j+1] == '<' and board[i][j-1] == '>'):
                    ans += 1
    print(ans)