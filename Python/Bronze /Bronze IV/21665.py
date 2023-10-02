h,w = map(int,input().split())
original = []
maya = []
ans = 0

for i in range(h):
    original.append(input())
input()
for i in range(h):
    maya.append(input())


for i in range(h):
    for j in range(w):
        if original[i][j] == maya[i][j]:
            ans += 1

print(ans)