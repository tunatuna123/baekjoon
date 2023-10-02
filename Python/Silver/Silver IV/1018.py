h,w = map(int,input().split())
chess = []
ans = []

for i in range(h):
    chess.append(input())

wb = [[] for i in range(h)]
for i in range(8):
    for j in range(8):
            if (i+j)%2 == 0:
                wb[i] += 'W'
            else:
                wb[i] += 'B'

bw = [[] for i in range(h)]
for i in range(8):
    for j in range(8):
            if (i+j)%2 == 0:
                bw[i] += 'B'
            else:
                bw[i] += 'W'

for i in range(h-8+1):
    for j in range(w-8+1):
        ans_1 = 0
        ans_2 = 0
        for k in range(8):
            for t in range(8):
                if chess[i+k][j+t] != wb[k][t]:
                    ans_1 += 1
                if chess[i+k][j+t] != bw[k][t]:
                    ans_2 += 1
        ans.append(ans_1)
        ans.append(ans_2)

print(min(ans))