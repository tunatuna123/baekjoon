n = int(input())
p = []
ans = []

for i in range(n):
    a,b = map(int,input().split())
    p.append((a,b))

for i in p:
    rank = 1
    for j in p:
        if j[0] > i[0] and j[1] > i[1]:
            rank += 1
    ans.append(rank)

print(' '.join(map(str,ans)))