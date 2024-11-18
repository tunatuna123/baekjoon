import sys
input = sys.stdin.readline

n = int(input())
stu = []
meets = [[0]*n for i in range(n)]

for i in range(n):
    stu.append(list(map(int,input().split())))

for i in range(5):
    for j in range(n):
        for k in range(j+1, n):
            if stu[j][i] == stu[k][i]:
                meets[k][j] = 1
                meets[j][k] = 1

ans = []
for i in range(n):
    ans.append(meets[i].count(1))

print(ans.index(max(ans))+1)