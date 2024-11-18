import sys
input = sys.stdin.readline

h,w = map(int,input().split())
castle = []
h_none,w_none = 0,0

for i in range(h):
    castle.append(list(input().strip()))

for i in range(h):
    if 'X' not in castle[i]:
        h_none += 1

for i in range(w):
    cnt = 0
    for j in range(h):
        if castle[j][i] == 'X':
            cnt += 1
    if cnt == 0:
        w_none += 1

print(max(h_none, w_none))