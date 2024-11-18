import sys
input = sys.stdin.readline

n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int,input().split())))

white = 0
blue = 0

def dfs(x,y,n):
    global white, blue
    color = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != paper[i][j]:
                dfs(x,y,n//2)
                dfs(x+n//2,y,n//2)
                dfs(x,y+n//2,n//2)
                dfs(x+n//2,y+n//2,n//2)
                return
    
    if color == 0:
        white += 1
    else:
        blue += 1

dfs(0,0,n)
print(white)
print(blue)